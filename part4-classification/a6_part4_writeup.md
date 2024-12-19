# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
Not as accurate, due to the difference in x-values inputed into the model. Without something to scale, the data will be much more vast which results in less accuracy.
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
More so than without, but still not good enough to use in a reliability sense. More data is likely needed to keep refining the model to make things more accurate.
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?
The model did generally well in predicting when they did and didn't purchase.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.
 She would not.
