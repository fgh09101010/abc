import matplotlib.pyplot as plt
from io import BytesIO
import base64

import matplotlib.dates as mdates   
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] 
def generate_time_axis(starts_at_list,name_list,ticket_left_list):
    plt.figure(figsize=(10, 4))
    plt.scatter(starts_at_list, name_list,s=50, marker='o')
    plt.xlabel('開始時間')
    plt.ylabel('音樂會')
    plt.title('音樂會開始時間、剩餘門票')
    x_values = mdates.date2num(starts_at_list)
    y_values = []
    y_name=[]
    j=-0.7
    for i in range(len(name_list)):
        if name_list[i] not in y_name:
            y_name.append(name_list[i])
            j+=1
            y_values.append(j)
        else:
            y_values.append(y_values[y_name.index(name_list[i])])
    for i, txt in enumerate(ticket_left_list):
        plt.text(x_values[i]-6, y_values[i], str(txt))
    plt.grid(True)

    plt.tight_layout()

    # 將圖片轉換為Base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return image_base64

def generate_price(name_list,ticket_price_list):
    plt.figure(figsize=(8, 6))
    plt.barh(name_list, ticket_price_list, color='skyblue')
    plt.xlabel('門票價格')
    plt.ylabel('音樂會')
    plt.title('音樂會門票價格')
    plt.grid(True)
    plt.tight_layout()

    # 將圖片轉換為Base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close()

    return image_base64