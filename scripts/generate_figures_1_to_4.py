import os
from itertools import combinations, product
from math import comb, sqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


IMAGE_DIR = ROOT / "images"
TOTAL_SCORE = 440
PASSING_SCORE = int(0.70 * TOTAL_SCORE)

COLORS = {
    "red": "#b91c1c",
    "blue": "#1d4ed8",
    "teal": "#0f766e",
    "gold": "#b7791f",
    "rose": "#be123c",
    "ink": "#202832",
}


def set_theme():
    sns.set_theme(
        context="talk",
        style="whitegrid",
        rc={
            "axes.facecolor": "#f7f3ed",
            "figure.facecolor": "#f7f3ed",
            "grid.color": "#d7cfc4",
            "axes.edgecolor": "#2f3842",
            "axes.labelcolor": COLORS["ink"],
            "axes.labelsize": 22,
            "axes.titlesize": 24,
            "xtick.color": COLORS["ink"],
            "xtick.labelsize": 18,
            "ytick.color": COLORS["ink"],
            "ytick.labelsize": 18,
            "legend.fontsize": 15,
            "font.family": "DejaVu Sans",
        },
    )


def finish(fig, ax, output_path):
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(output_path, dpi=220, bbox_inches="tight")
    plt.close(fig)


def binomial_score_pmf(n, p, points):
    pmf = np.zeros(n * points + 1)
    for k in range(n + 1):
        pmf[k * points] = comb(n, k) * p**k * (1 - p) ** (n - k)
    return pmf


def repeated_question_pmf(single_question_pmf, n):
    total = np.array([1.0])
    for _ in range(n):
        total = np.convolve(total, single_question_pmf)
    return total


def figure_1():
    output_path = IMAGE_DIR / "random_guesser_question_type_distributions.png"
    tf_pmf = binomial_score_pmf(70, 1 / 2, 2)
    c15_pmf = binomial_score_pmf(15, 1 / 5, 10)

    c25_single = np.zeros(11)
    c25_single[0] = 3 / 10
    c25_single[5] = 6 / 10
    c25_single[10] = 1 / 10
    c25_pmf = repeated_question_pmf(c25_single, 15)

    question_types = {
        "TF": {"pmf": tf_pmf, "color": COLORS["blue"]},
        "C15": {"pmf": c15_pmf, "color": COLORS["gold"]},
        "C25": {"pmf": c25_pmf, "color": COLORS["teal"]},
    }

    total_pmf = np.convolve(np.convolve(tf_pmf, c15_pmf), c25_pmf)
    total_scores = np.arange(len(total_pmf))
    pass_probability = total_pmf[PASSING_SCORE:].sum()

    fig, ax = plt.subplots(figsize=(12, 7))
    ax.fill_between(
        total_scores,
        total_pmf,
        color=COLORS["red"],
        alpha=0.34,
        label="Total",
    )
    ax.plot(total_scores, total_pmf, color=COLORS["red"], linewidth=2.4)

    for name, q in question_types.items():
        scores = np.nonzero(q["pmf"])[0]
        probs = q["pmf"][scores]
        ax.plot(
            scores,
            probs,
            marker="o",
            linewidth=2.1,
            markersize=4,
            color=q["color"],
            label=name,
        )

    ax.axvline(
        PASSING_SCORE,
        color=COLORS["ink"],
        linestyle="--",
        linewidth=2.2,
        label="Passing line",
    )
    ax.text(
        PASSING_SCORE + 4,
        ax.get_ylim()[1] * 0.45,
        f"P(pass) = {pass_probability:.2e}",
        ha="left",
        va="center",
        fontsize=16,
        color=COLORS["ink"],
    )
    ax.set_title("Exact Random-Guesser Score Distributions", loc="left", pad=14, fontweight="bold")
    ax.set_xlabel("Score from random guessing (points)")
    ax.set_ylabel("Probability")
    ax.set_xlim(0, TOTAL_SCORE)
    ax.legend(frameon=False, loc="upper right")
    finish(fig, ax, output_path)


def c25_single_question_pmf(p):
    true_statements = {0, 1}
    score_probs = {0: 0.0, 5: 0.0, 10: 0.0}

    for judged_true_bits in product([False, True], repeat=5):
        judged_true = {i for i, bit in enumerate(judged_true_bits) if bit}
        judged_false = set(range(5)) - judged_true

        prob = 1.0
        for i, bit in enumerate(judged_true_bits):
            actual_true = i in true_statements
            prob *= p if bit == actual_true else 1 - p

        if len(judged_true) < 2:
            selected_sets = [
                judged_true | set(extra)
                for extra in combinations(judged_false, 2 - len(judged_true))
            ]
        else:
            selected_sets = [set(choice) for choice in combinations(judged_true, 2)]

        for selected in selected_sets:
            n_correct = len(selected & true_statements)
            score_probs[5 * n_correct] += prob / len(selected_sets)

    return score_probs


def c25_mean_std(p):
    score_probs = c25_single_question_pmf(p)
    mean_one = sum(score * prob for score, prob in score_probs.items())
    second_moment_one = sum(score**2 * prob for score, prob in score_probs.items())
    var_one = second_moment_one - mean_one**2
    return 15 * mean_one, np.sqrt(15 * var_one)


def figure_2():
    output_path = IMAGE_DIR / "tf_c15_c25_informed_guesser_sensitivity.png"

    p_tf = np.arange(0.5, 1, 0.01)
    p_15 = np.arange(0.2, 1, 0.01)
    p_25 = np.arange(0.5, 1, 0.01)

    mean_tf = 70 * p_tf * 2
    std_tf = 2 * np.sqrt(70 * p_tf * (1 - p_tf))
    mean_c15 = 15 * p_15 * 10
    std_c15 = 10 * np.sqrt(15 * p_15 * (1 - p_15))
    mean_c25 = np.array([c25_mean_std(p)[0] for p in p_25])
    std_c25 = np.array([c25_mean_std(p)[1] for p in p_25])

    fig, ax = plt.subplots(figsize=(10, 6))
    series = [
        ("TF", p_tf, mean_tf, std_tf, COLORS["blue"]),
        ("C15", p_15, mean_c15, std_c15, COLORS["gold"]),
        ("C25", p_25, mean_c25, std_c25, COLORS["teal"]),
    ]
    for name, p_grid, mean, std, color in series:
        ax.plot(p_grid, mean, color=color, linewidth=2.5, label=f"Expected {name} score")
        ax.fill_between(
            p_grid,
            mean - std,
            mean + std,
            color=color,
            alpha=0.18,
            label=f"{name} +/- 1 std",
        )

    ax.set_title("Expected Score", loc="left", pad=14, fontweight="bold")
    ax.set_xlabel("Probability of answering correctly (p)")
    ax.set_ylabel("Score (points)")
    ax.legend(frameon=False, loc="upper left")
    finish(fig, ax, output_path)


def c25_selected_sets(judged_true):
    judged_true = set(judged_true)
    judged_false = set(range(5)) - judged_true
    if len(judged_true) < 2:
        return [
            judged_true | set(extra)
            for extra in combinations(judged_false, 2 - len(judged_true))
        ]
    return [set(choice) for choice in combinations(judged_true, 2)]


def c25_score(selected):
    return 5 * len(set(selected) & {0, 1})


def c25_gain_mean_std(p, step=0.01):
    p_next = min(p + step, 1.0)
    dp = p_next - p
    gain_probs = {}
    state_probs = [p, dp, 1 - p_next]

    for states in product([0, 1, 2], repeat=5):
        prob = np.prod([state_probs[s] for s in states])
        if prob == 0:
            continue

        judged_true_before = set()
        judged_true_after = set()
        for i, state in enumerate(states):
            actual_true = i in {0, 1}
            correct_before = state == 0
            correct_after = state in {0, 1}
            before_judgment_true = actual_true if correct_before else not actual_true
            after_judgment_true = actual_true if correct_after else not actual_true

            if before_judgment_true:
                judged_true_before.add(i)
            if after_judgment_true:
                judged_true_after.add(i)

        before_sets = c25_selected_sets(judged_true_before)
        after_sets = c25_selected_sets(judged_true_after)

        for before_selected in before_sets:
            before_score = c25_score(before_selected)
            for after_selected in after_sets:
                after_score = c25_score(after_selected)
                gain = after_score - before_score
                gain_probs[gain] = gain_probs.get(gain, 0.0) + prob / (
                    len(before_sets) * len(after_sets)
                )

    mean_one = sum(gain * prob for gain, prob in gain_probs.items())
    second_moment_one = sum(gain**2 * prob for gain, prob in gain_probs.items())
    var_one = second_moment_one - mean_one**2
    return 15 * mean_one, np.sqrt(15 * var_one)


def bernoulli_gain_mean_std(n, points, p, step=0.01):
    p_next = min(p + step, 1.0)
    dp = p_next - p
    mean = n * points * dp
    std = points * np.sqrt(n * dp * (1 - dp))
    return mean, std


def figure_3():
    output_path = IMAGE_DIR / "question_type_point_sensitivity.png"
    step = 0.01
    series = {
        "TF": (np.arange(0.5, 1, step), lambda p: bernoulli_gain_mean_std(70, 2, p, step), COLORS["blue"]),
        "C15": (np.arange(0.2, 1, step), lambda p: bernoulli_gain_mean_std(15, 10, p, step), COLORS["gold"]),
        "C25": (np.arange(0.5, 1, step), lambda p: c25_gain_mean_std(p, step), COLORS["teal"]),
    }

    fig, ax = plt.subplots(figsize=(10, 6))
    for name, (p_grid, gain_fn, color) in series.items():
        values = np.array([gain_fn(p) for p in p_grid])
        ax.plot(p_grid, values[:, 0], color=color, linewidth=2.5, label=name)

    ax.axhline(0, color=COLORS["ink"], linewidth=1.0, alpha=0.55)
    ax.set_title("Point Gain from a 1% Improvement in p", loc="left", pad=14, fontweight="bold")
    ax.set_xlabel("Current probability of answering correctly (p)")
    ax.set_ylabel("Expected score gain")
    ax.legend(frameon=False)
    finish(fig, ax, output_path)


def normalized_payoff_pmf(n):
    k = np.arange(n + 1)
    payoffs = (2 * k - n) / n
    probs = np.array([comb(n, int(i)) / (2**n) for i in k], dtype=float)
    return payoffs, probs


def pmf_to_density(x, p):
    dx = x[1] - x[0]
    return dx, p / dx


def figure_4():
    output_path = IMAGE_DIR / "coin_flip_normalized_payoff.png"
    short_x, short_p = normalized_payoff_pmf(20)
    mid_x, mid_p = normalized_payoff_pmf(400)
    long_x, long_p = normalized_payoff_pmf(2000)
    short_dx, short_density = pmf_to_density(short_x, short_p)
    mid_dx, mid_density = pmf_to_density(mid_x, mid_p)
    long_dx, long_density = pmf_to_density(long_x, long_p)

    fig, ax = plt.subplots(figsize=(10.5, 4.2))
    ax.bar(
        short_x,
        short_density,
        width=short_dx,
        color=COLORS["red"],
        alpha=0.30,
        edgecolor=COLORS["red"],
        linewidth=1.0,
        label="20 games",
        align="center",
    )
    ax.bar(
        mid_x,
        mid_density,
        width=mid_dx,
        color=COLORS["blue"],
        alpha=0.32,
        edgecolor=COLORS["blue"],
        linewidth=0.32,
        label="400 games",
        align="center",
    )
    ax.bar(
        long_x,
        long_density,
        width=long_dx,
        color=COLORS["teal"],
        alpha=0.50,
        edgecolor=COLORS["teal"],
        linewidth=0.18,
        label="2000 games",
        align="center",
    )
    ax.axvline(0, color=COLORS["ink"], linewidth=1.1, alpha=0.55)
    ax.set_xlim(-1.05, 1.05)
    ax.set_ylim(0, 19)
    ax.set_xlabel("Normalized payoff  $S_n / N$")
    ax.set_ylabel("Density")
    ax.legend(frameon=False)
    finish(fig, ax, output_path)


def main():
    IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    set_theme()
    figure_1()
    figure_2()
    figure_3()
    figure_4()
    print("Saved Figures 1-4 with the shared calm theme.")


if __name__ == "__main__":
    main()
