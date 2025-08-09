name = "传智播客"       #公司名
stock_price = 19.99   #当前股价
stock_code = "003032"   #股票代码
stock_price_daily_growth_factor =   1.2    #每日股票增长系数
growth_day = 7   #增长天数

all_price = stock_price * stock_price_daily_growth_factor ** growth_day


print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price},每日增长系数是：{stock_price_daily_growth_factor},经过{growth_day}天的增长后，股价达到了:{all_price:.2f}")

