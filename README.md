# Stock Price Notifier
### [Zagreb Stock Exchange](https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6)
### Sends notification when the CBX index trend changes to the certain value

## Usage
Takes two arguments: trend direction and expected trend value

Trend direction:
gt - greater then, 
lt - less then.

Trend value: float number

### CLI command example
```
python main.py gt -0.1
```
Here the application will send a notification email, when the trend reaches up 
to the value -0.1