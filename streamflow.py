
import numpy as np
import matplotlib.pyplot as plt


# load river data
def load_streamflow(filename):
    data = np.genfromtxt(filename, delimiter=",", dtype=str, skip_header=1)

    dates = data[:, 0]
    flows = data[:, 1:6].astype(float)

    return dates, flows


# make the river graph

def summarize(dates, flows, sites):
    # Excel check for 10163000: max = 131.0, avg = 57.0
    # river flow summary
    print("Gauge       Max (cfs)    Date of max           Min (cfs)    Avg (cfs)")

    with open("streamflow_summary.csv", "w") as file:
        file.write("Gauge,Max (cfs),Date of max,Min (cfs),Avg (cfs)\n")

        for i in range(len(sites)):
            max_flow = np.max(flows[:, i])
            min_flow = np.min(flows[:, i])
            avg_flow = np.mean(flows[:, i])

            max_row = np.argmax(flows[:, i])
            max_date = dates[max_row]

            print(f"{sites[i]:<12}{max_flow:<13.1f}{max_date:<22}{min_flow:<13.1f}{avg_flow:.1f}")

            file.write(f"{sites[i]},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.1f}\n")

def plot_streamflow(dates, flows, sites):
    plt.figure(figsize=(10, 6))

    plt.plot(dates, flows[:, 0], label="Site " + sites[0])
    plt.plot(dates, flows[:, 1], label="Site " + sites[1])
    plt.plot(dates, flows[:, 2], label="Site " + sites[2])
    plt.plot(dates, flows[:, 3], label="Site " + sites[3])
    plt.plot(dates, flows[:, 4], label="Site " + sites[4])

    # labels
    plt.title("Provo River Streamflow June 2021")
    plt.xlabel("Date")
    plt.ylabel("Streamflow (cfs)")

    plt.xticks(range(0, len(dates), 96), dates[::96], rotation=45)

    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()


# main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]

dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")

plot_streamflow(dates, flows, sites)
summarize(dates, flows, sites)
