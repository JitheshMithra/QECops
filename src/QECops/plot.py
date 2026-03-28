#cli input tool that prints values and saves a png + an interactive plot
<<<<<<< HEAD:src/QECops/plot.py
#Example cli: cd src/ python -m QECops.plot --n 3 5 7 --trials 10000 --seed 0 --logicalbit 0 --pmin 0.0 --pmax 0.2 --pstep 0.02
=======
#Example cli: cd src/ python -m QECsim.plot --n 3 5 7 --trials 10000 --seed 0 --logicalbit 0 --pmin 0.0 --pmax 0.2 --pstep 0.02
>>>>>>> b0f1821aecba966dd67fac14d97b2daaee7a9c75:src/QECsim/plot.py
import argparse
from datetime import datetime
from pathlib import Path

from .analytical import analytical_logical_error
from .simulation import psweep
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def argparser():
    parser=argparse.ArgumentParser()
    parser.add_argument("--n", nargs="+",type=int, required=True)
    parser.add_argument("--trials",type=int,default=10000)
    parser.add_argument("--seed",type=int,default=0)
    parser.add_argument("--logicalbit",type=int,choices=[0,1],default=0)
    parser.add_argument("--pmin",type=float,default=0.0)
    parser.add_argument("--pmax",type=float,default=0.2)
    parser.add_argument("--pstep",type=float,default=0.02)
    return parser.parse_args()

def pvaluesgen(pmin, pmax, pstep):
    if pstep <=0:
        raise ValueError("pstep must be positive")
    if pmin <0 or pmax>1 or pmin>pmax:
        raise ValueError("pmin and pmax must be between 0 and 1 and pmin must be less than or equal to pmax")
   
    pvalues=[]
    p=pmin
    while p <= pmax+ 1e-12:
        pvalues.append(round(p,12))
        p=p + pstep
    return pvalues

def plotrun(nvalues,pvalues,trials,seed,logicalbit):
    #odd n values are required
    for n in nvalues:
        if n<=0:
            raise ValueError("n values must be positive")
        if n%2==0:
            raise ValueError("n values must be odd")
   
    #results folder saving
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    resultsdir = Path("results") /run_id
    resultsdir.mkdir(parents=True)

    allresults={}

    #runs simulations
    for n in nvalues:
        allresults[n]= psweep(n, pvalues, trials, seed, logicalbit)
   
    #table outputs
    print("n p logical_error_rate")
    with open(resultsdir/"QECops_noise_results.txt", "w") as f:
        f.write("n p logical_error_rate analytical_logical_error\n")
        for n in nvalues:
            for p, ler in allresults[n]:
                analytic = analytical_logical_error(n, p)
                line = f"{n} {p:.2f} {ler:.6f} {analytic:.6f}"
                print(line)
                f.write(line+"\n")
   
    #plot saving as png
    for n in nvalues:
        results = allresults[n]
        
        x=[p for p, ler in results]
        ysim=[ler for p, ler in results]
        
        yanalytics=[]
        
        for p in x:
            yanalytics.append(analytical_logical_error(n, p))
        
        plt.plot(x,ysim,marker='o', label="n="+str(n)+" Monte Carlo")
        plt.plot(x,yanalytics, linestyle='--', label='n=' +str(n)+" Analytical")
        
        
    plt.xlabel("Physical error rate (p)")
    plt.ylabel("Logical error rate")
    plt.legend(title="Repetition code length (n)")
    plt.savefig(resultsdir/"plot.png", dpi=300, bbox_inches="tight")
    plt.close()

    # interactive plot
    fig = go.Figure()

    for n in nvalues:
        results = allresults[n]

        x = [p for p, ler in results]
        ysim = [ler for p, ler in results]

        yanalytics = []
        for p in x:
            yanalytics.append(analytical_logical_error(n, p))

        # Monte Carlo
        fig.add_trace(go.Scatter(
            x=x,
            y=ysim,
            mode='lines+markers',
            name="n=" + str(n) + " Monte Carlo"
        ))

        # Analytical
        fig.add_trace(go.Scatter(
            x=x,
            y=yanalytics,
            mode='lines',
            line=dict(dash='dash'),
            name="n=" + str(n) + " Analytical"
        ))

    fig.update_layout(
        xaxis_title="Physical error rate (p)",
        yaxis_title="Logical error rate",
        hovermode="x unified",
    )

    fig.write_html(resultsdir/"plot.html")
        
def main():
    args = argparser()
    pvalues = pvaluesgen(args.pmin, args.pmax, args.pstep)
    plotrun(args.n, pvalues, args.trials, args.seed, args.logicalbit)
    print("Check 'results' folder within the src package for saved plots")

if __name__ == "__main__":
    main()
