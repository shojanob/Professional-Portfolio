import pandas

squirrel_data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
color_fur_list = squirrel_data["Primary Fur Color"].tolist()
amount_cinnamon = 0
amount_gray = 0
amount_black = 0
amount_nan = 0


for fur in color_fur_list:
    if fur == "Gray":
        amount_gray += 1
    elif fur == "Cinnamon":
        amount_cinnamon += 1
    elif fur == "Black":
        amount_black += 1
    else:
        amount_nan += 1


squirrel_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [amount_gray, amount_cinnamon, amount_black]
}
data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_count.csv")