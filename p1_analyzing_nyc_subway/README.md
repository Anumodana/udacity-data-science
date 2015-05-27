# Analyzing the NYC Subway Dataset

## Section 1. Statistical Test

#### 1.1 Which statistical test did you use to analyze the NYC subway data? Did you use a one-tail or a two-tail P value? What is the null hypothesis? What is your p-critical value?

I used the Mann Whitney U-test to analyze the NYC subway data. I used a two-tail P value.
The null hypothesis is that two populations on rainy and non-rainy days have the same mean.
My p-critical value is 0.05.

> To get the two-sided P value, the P value returned by scipy.stats.mannwhitneyu must be multiplied by 2.

#### 1.2 Why is this statistical test applicable to the dataset? In particular, consider the assumptions that the test is making about the distribution of ridership in the two samples.

Because rainy and non-rainy days histograms are not normally distributed as shown in section 3.1 and
the Mann Whitney U-test is suitable for testing two populations with unknown distributions.

#### 1.3 What results did you get from this statistical test? These should include the following numerical values: p-values, as well as the means for each of the two samples under test.

+ Mean entries with rain = 1105.4463767458733
+ Mean entries without rain = 1090.278780151855
+ U = 1924409167.0
+ p-value = 0.024999912793489721 ~ 0.025

#### 1.4 What is the significance and interpretation of these results?

The null hypothesis is rejected due to 0.025 < 0.05 indicates that
there is a statistically significant difference in ridership between
rainy and non-rainy days.

## Section 2. Linear Regression

#### 2.1 What approach did you use to compute the coefficients theta and produce prediction for ENTRIESn_hourly in your regression model:
+ Gradient descent (as implemented in exercise 3.5)
+ OLS using Statsmodels
+ Or something different?

I used OLS using Statsmodels.

#### 2.2 What features (input variables) did you use in your model? Did you use any dummy variables as part of your features?

The features I used in the model were "rain", "Hour", "meantempi", "meanpressurei", and "meanwindspdi". "UNIT" was used as the dummy variable.

#### 2.3 Why did you select these features in your model? We are looking for specific reasons that lead you to believe that the selected features will contribute to the predictive power of your model.

I thought that these features may affect people’s decision for riding or not riding the NYC subway. Initially, I used "rain" with "UNIT" dummy variable in the model and then I got the R-squared value 0.418. After that, I included "Hour" and it improved the R-squared value to 0.458. Finally, I decided to include "meantempi", "meanpressurei", and "meanwindspdi" to the model and then the R-squared value was improved to 0.459.

#### 2.4 What are the coefficients (or weights) of the non-dummy features in your linear regression model?

+ rain: -18.1987
+ Hour: 67.4003
+ meantempi: -5.6176
+ meanpressurei: -265.8013
+ meanwindspdi: 21.6812

#### 2.5 What is your model’s R2 (coefficients of determination) value?

The R squared value is 0.459.

#### 2.6 What does this R2 value mean for the goodness of fit for your regression model? Do you think this linear model to predict ridership is appropriate for this dataset, given this R2 value?

From the R squared value, 45.9% of the variance can be explained by the regression model. Given the R squared value and the following graphs, I think this linear model to predict ridership isn’t appropriate for this dataset.

![](https://raw.githubusercontent.com/Anumodana/udacity-data-science/master/p1_analyzing_nyc_subway/images/Histogram%20of%20Residuals.png)

![](https://raw.githubusercontent.com/Anumodana/udacity-data-science/master/p1_analyzing_nyc_subway/images/Predicted%20vs%20Actual%20ENTRIESn_hourly.png)

![](https://raw.githubusercontent.com/Anumodana/udacity-data-science/master/p1_analyzing_nyc_subway/images/Residuals%20vs%20Index.png)

## Section 3. Visualization

#### 3.1 One visualization should contain two histograms: one of  ENTRIESn_hourly for rainy days and one of ENTRIESn_hourly for non-rainy days.

![](https://raw.githubusercontent.com/Anumodana/udacity-data-science/master/p1_analyzing_nyc_subway/images/ENTRIESn_hourly%20histogram.png)

From the above data visualization, it indicates that the ridership for non-rainy days and rainy days is not normally distributed.
Moreover, the frequency of ENTRIESn_hourly for non-rainy days is higher than rainy days.

#### 3.2 One visualization can be more freeform.

![](https://raw.githubusercontent.com/Anumodana/udacity-data-science/master/p1_analyzing_nyc_subway/images/average_entries_per_day.png)

The above data visualization shows the average subway ridership by hour in each day.
Few people ride the NYC subway system between 2am and 7am everyday.
Over 2,500 people ride the NYC subway system at 12pm and 8pm on weekdays.
Moreover, the graph also indicates that more people ride the NYC subway system on weekdays than on weekends.

## Section 4. Conclusion

#### 4.1 From your analysis and interpretation of the data, do more people ride  the NYC subway when it is raining or when it is not raining?

From the analysis and interpretation of the data, rain and non-rainy days effect to the ridership.
There is a higher chance that more people ride the NYC subway on rainy days than on non-rainy days.

#### 4.2 What analyses lead you to this conclusion? You should use results from both your statistical tests and your linear regression to support your analysis.

From the analyses, the null hypothesis that two populations between rainy and non-rainy days have the same mean was rejected
due to the p-value, 0.025, is less than the p-critical value, 0.05. The mean of ENTRIESn_hourly on rainy and non-rainy days
are 1105.446 and 1090.279 respectively. Thus, there is a higher chance that more people ride the NYC subway on rainy days than on non-rainy days.

## Section 5. Reflection

#### 5.1 Please discuss potential shortcomings of the methods of your analysis.

**Dataset**
+ Only data on May 2011 included in the dataset that I analyzed.
If the sample size of data is increased, the analysis may be changed.
+ The number of ridership who rides the NYC subway may be changed
depends on several factors other than the weather.

**Analysis**
+ From section 2.6, we can see that the linear model is not a good fit to this dataset. It seems data appears to be non-linear. They are not symmetrically distributed in the Residuals graph. We may try to analyze data by using non-linear model instead.

## References

+ http://pandas.pydata.org/pandas-docs/stable/visualization.html
+ https://github.com/yhat/ggplot
+ http://statsmodels.sourceforge.net/devel/examples/notebooks/generated/ols.html
+ http://graphpad.com/guides/prism/6/statistics/index.htm?one-tail_vs__two-tail_p_values.htm
