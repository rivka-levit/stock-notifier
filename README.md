# Stock Price Notifier
### [Zagreb Stock Exchange](https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6)
![cbx_trend2](https://github.com/rivka-levit/stock-notifier/assets/122191238/0f958025-016b-4415-b79b-20e5e669b5ea)
### Sends a notification when the CBX index trend changes to a certain value

## Usage
Takes two arguments: trend direction and expected trend value

Trend direction:
gt - greater then 
lt - less then.

Trend value: float number

### CLI command example
```
python main.py gt -0.1
```
Here the application will send a notification email when the trend reaches up 
to the value -0.1
