# These are the vizualization functions that are used for testing

# Import packages
import pandas as pd
from players import (
    CageyListener,
    DupSpeaker,
    HonestDivSpeaker,
    HonestNdivSpeaker,
    HonestNdivSpeakerPlus,
    Listener,
    Player,
)
import matplotlib.pyplot as plt


# Viz functions for the RSA testing part of the presentation of the model


def lis_viz(
    l0: Player or Listener or CageyListener,
    socs: list,
    lexs: list,
    interpretation="world_interpretation",
):
    l0_preds = {
        k: v[interpretation] for (k, v) in l0.full_predictions(socs, lexs).items()
    }

    df = pd.DataFrame.from_dict(l0_preds)
    ax = df.plot.bar(rot=0)
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.0),
        ncol=3,
        fancybox=True,
        shadow=True,
    )
    ax.set(xlabel="Message", ylabel="P(w|m)", title="RSA predictions for the listener")
    ax.set_ylim([0, 1])
    plt.show()


def speak_viz(
    s1: HonestNdivSpeaker or HonestNdivSpeakerPlus or HonestDivSpeaker or DupSpeaker,
    socs: list,
    lexs: list,
):
    s1_preds = s1.full_predictions(socs, lexs)
    df = pd.DataFrame.from_dict(s1_preds, orient="index")
    ax = df.plot.bar(rot=0)
    ax.legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.0),
        ncol=3,
        fancybox=True,
        shadow=True,
    )
    ax.set(xlabel="Message", ylabel="P(m|w)", title="RSA predictions for the speaker")
    ax.set_ylim([0, 1])
    plt.show()
