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
import tikzplotlib


# Viz functions for the RSA testing part of the presentation of the model


def lis_viz(
    lis: Player or Listener or CageyListener,
    socs: list,
    lexs: list,
    interpretation="world_interpretation",
):
    lis_preds = {
        k: v[interpretation] for (k, v) in lis.full_predictions(socs, lexs).items()
    }

    df = pd.DataFrame.from_dict(lis_preds)
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

def lis_viz_save(
    lis : Player or Listener or CageyListener,
    socs : list, 
    lexs : list,
    savename : str, 
    interpretation = "world_interpretation"
):
    lis_preds = {
        k: v[interpretation] for (k, v) in lis.full_predictions(socs, lexs).items()
    }

    df = pd.DataFrame.from_dict(lis_preds)
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
    tikzplotlib.save(savename)

def speak_viz(
    s1: HonestNdivSpeaker or HonestNdivSpeakerPlus or HonestDivSpeaker or DupSpeaker,
    socs: list,
    lexs: list,
):
    if type(s1) == DupSpeaker:
        s1_preds = s1.full_predictions(socs, lexs)[0]
    else:
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

def speak_viz_save(
    s1: HonestNdivSpeaker or HonestNdivSpeakerPlus or HonestDivSpeaker or DupSpeaker,
    socs: list,
    lexs: list,
    savename: str,
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
    tikzplotlib.save(savename)