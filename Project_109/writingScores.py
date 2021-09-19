import statistics
import math
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("StudentsPerformance.csv")
writingScores = df["writing score"].to_list()

mean = statistics.mean(writingScores)
median = statistics.median(writingScores)
mode = statistics.mode(writingScores)
print(mean, median, mode)

def standardDeviation():
    numeratorPart = 0
    for y in writingScores:
        numeratorPart += (y - mean)**2

    standardDeviation = math.sqrt(numeratorPart/len(writingScores))
    return standardDeviation
stdDeviation = standardDeviation()
print(stdDeviation)

sigmaStart, sigmaEnd = mean - stdDeviation, mean + stdDeviation
sigma2Start, sigma2End = mean - 2*stdDeviation, mean + 2*stdDeviation
sigma3Start, sigma3End = mean - 3*stdDeviation, mean + 3*stdDeviation
print(sigmaStart, sigmaEnd, sigma2Start, sigma2End, sigma3Start, sigma3End)

figure = ff.create_distplot([writingScores], ["Result"], show_hist = False)
figure.add_trace(go.Scatter(x = [mean, mean], y = [0, 0.17], mode = "lines", name = "Mean"))
figure.add_trace(go.Scatter(x = [sigmaStart, sigmaStart], y = [0,0.17], mode = "lines", name = "One Standard Deviation"))
figure.add_trace(go.Scatter(x = [sigmaEnd, sigmaEnd], y = [0,0.17], mode = "lines", name = "Negative One Standard Deviation"))
figure.add_trace(go.Scatter(x = [sigma2Start, sigma2Start], y = [0,0.17], mode = "lines", name = "Two Standard Deviation"))
figure.add_trace(go.Scatter(x = [sigma2End, sigma2End], y = [0,0.17], mode = "lines", name = "Negative Two Standard Deviation"))
figure.add_trace(go.Scatter(x = [sigma3Start, sigma3Start], y = [0,0.17], mode = "lines", name = "Three Standard Deviation"))
figure.add_trace(go.Scatter(x = [sigma3End, sigma3End], y = [0,0.17], mode = "lines", name = "Negative Three Standard Deviation"))
figure.show()

sigmaResults = [result for result in writingScores if result > sigmaStart and result < sigmaEnd]
sigma2Results = [result2 for result2 in writingScores if result2 > sigma2Start and result2 < sigma2End]
sigma3Results = [result3 for result3 in writingScores if result3 > sigma3Start and result3 < sigma3End]

sigmaPercentage = len(sigmaResults)/len(writingScores)*100
sigma2Percentage = len(sigma2Results)/len(writingScores)*100
sigma3Percentage = len(sigma3Results)/len(writingScores)*100
print(sigmaPercentage, sigma2Percentage, sigma3Percentage)