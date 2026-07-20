import os
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".mplconfig"))

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np
import seaborn as sns

N_PEOPLE = 1000
INITIAL_WEALTH = 100
BET = 1
N_GAMES = 10_000_000
TRACK_EVERY = 10_000
SEED = 42

CACHE_PATH = ROOT / "data" / "wealth_rps_trajectories.npz"
OUTPUT_PATH = ROOT / "images" / "wealth_rps_trajectories.png"


def simulate_trajectories():
    rng = np.random.default_rng(SEED)
    wealth = np.full(N_PEOPLE, INITIAL_WEALTH, dtype=np.int32)
    games = np.arange(0, N_GAMES + 1, TRACK_EVERY, dtype=np.int32)
    trajectories = np.empty((len(games), N_PEOPLE), dtype=np.int32)
    trajectories[0] = wealth
    snapshot_i = 1

    for game in range(1, N_GAMES + 1):
        i, j = rng.choice(N_PEOPLE, size=2, replace=False)
        winner, loser = (i, j) if rng.random() < 0.5 else (j, i)

        if wealth[loser] > 0:
            wealth[loser] -= BET
            wealth[winner] += BET

        if game % TRACK_EVERY == 0:
            trajectories[snapshot_i] = wealth
            snapshot_i += 1

    top_people = np.argsort(wealth)[-10:][::-1]
    return games, trajectories, wealth, top_people


def load_or_create_cache():
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)

    if CACHE_PATH.exists():
        with np.load(CACHE_PATH) as cache:
            return (
                cache["games"],
                cache["trajectories"],
                cache["final_wealth"],
                cache["top_10"],
                True,
            )

    games, trajectories, final_wealth, top_people = simulate_trajectories()
    np.savez_compressed(
        CACHE_PATH,
        games=games,
        trajectories=trajectories,
        final_wealth=final_wealth,
        top_10=top_people,
        n_people=N_PEOPLE,
        initial_wealth=INITIAL_WEALTH,
        bet=BET,
        n_games=N_GAMES,
        track_every=TRACK_EVERY,
        seed=SEED,
    )
    return games, trajectories, final_wealth, top_people, False


def draw_plot(games, trajectories, final_wealth, top_people):
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    highlighted_people = top_people[:5]

    sns.set_theme(
        context="talk",
        style="whitegrid",
        rc={
            "axes.facecolor": "#f7f3ed",
            "figure.facecolor": "#f7f3ed",
            "grid.color": "#d7cfc4",
            "axes.edgecolor": "#2f3842",
            "axes.labelcolor": "#202832",
            "xtick.color": "#202832",
            "ytick.color": "#202832",
            "font.family": "DejaVu Sans",
        },
    )

    fig, (ax, hist_ax) = plt.subplots(
        1,
        2,
        figsize=(13, 7),
        dpi=150,
        sharey=True,
        gridspec_kw={"width_ratios": [5.6, 1.15], "wspace": 0.035},
        constrained_layout=True,
    )
    highlighted = set(highlighted_people.tolist())
    for person_i in range(N_PEOPLE):
        if person_i not in highlighted:
            ax.plot(
                games,
                trajectories[:, person_i],
                color="#0f766e",
                alpha=0.030,
                linewidth=0.50,
            )

    highlight_colors = [
        "#b91c1c",
        "#d97706",
        "#7c3aed",
        "#2563eb",
        "#db2777",
        "#16a34a",
        "#be123c",
        "#0891b2",
        "#9333ea",
        "#ca8a04",
    ]
    for rank, person_i in enumerate(highlighted_people, start=1):
        ax.plot(
            games,
            trajectories[:, person_i],
            color=highlight_colors[rank - 1],
            alpha=0.95,
            linewidth=1.9,
            label=f"#{rank}: person {person_i} (${final_wealth[person_i]:,})",
        )

    ax.axhline(
        INITIAL_WEALTH,
        color="#1d4ed8",
        linewidth=2.2,
        linestyle="--",
        label="Initial wealth ($100)",
    )
    ax.set_title(
        "Individual Wealth Trajectories Across Fair Random Exchange",
        loc="left",
        pad=16,
        fontweight="bold",
    )
    ax.set_xlabel("Number of games")
    ax.set_ylabel("Wealth ($)")
    ax.set_xlim(0, N_GAMES)
    ax.set_ylim(bottom=0)
    ax.xaxis.set_major_formatter(FuncFormatter(lambda x, pos: f"{x / 1_000_000:g} Mil"))
    ax.legend(
        frameon=False,
        loc="upper left",
        fontsize=8,
    )
    ax.spines[["top", "right"]].set_visible(False)

    bins = np.arange(0, max(601, final_wealth.max() + 31), 30)
    hist_ax.hist(
        final_wealth,
        bins=bins,
        orientation="horizontal",
        density=True,
        color="#0f766e",
        edgecolor="#f7f3ed",
        linewidth=1.0,
        alpha=0.78,
    )
    for person_i in highlighted_people:
        hist_ax.axhline(
            final_wealth[person_i],
            color="#202832",
            alpha=0.35,
            linewidth=0.7,
        )

    hist_ax.axhline(
        INITIAL_WEALTH,
        color="#1d4ed8",
        linewidth=2.2,
        linestyle="--",
    )
    hist_ax.set_xlabel("Density")
    hist_ax.set_ylabel("")
    hist_ax.tick_params(axis="y", left=False, labelleft=False)
    hist_ax.tick_params(axis="x", bottom=False, labelbottom=False)
    hist_ax.spines[["top", "right", "left"]].set_visible(False)

    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)


def main():
    start = time.time()
    games, trajectories, final_wealth, top_people, loaded = load_or_create_cache()
    draw_plot(games, trajectories, final_wealth, top_people)

    source = "loaded" if loaded else "created"
    print(f"Cache {source}: {CACHE_PATH}")
    print(f"Saved plot: {OUTPUT_PATH}")
    print(f"Top 5 people: {top_people[:5].tolist()}")
    print(f"Top 5 final wealth: {[int(final_wealth[i]) for i in top_people[:5]]}")
    print(f"Elapsed: {time.time() - start:.1f}s")


if __name__ == "__main__":
    main()
