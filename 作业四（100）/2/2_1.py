import pandas as pd
import folium
from folium.plugins import HeatMap
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageDraw, ImageFont
import time

# 读取Excel数据
file_path = "jd起点.xlsx"
df = pd.read_excel(file_path)

# 过滤有效的经纬度数据
df = df.dropna(subset=['wgs_s_lng', 'wgs_s_lat'])

# 加载嘉定区GeoJSON文件
geojson_file = "jiading.geojson"
with open(geojson_file, 'r', encoding='utf-8') as f:
    jiading_geojson = json.load(f)

# 创建基础地图，中心点聚焦嘉定区
m = folium.Map(location=[31.3833, 121.2500], zoom_start=13)

# 添加嘉定区GeoJSON边界
geo_json_layer = folium.GeoJson(
    jiading_geojson,
    name="嘉定区边界",
    style_function=lambda x: {
        'fillColor': 'green',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.1,
    }
).add_to(m)

# 自动调整地图到嘉定区范围
m.fit_bounds(geo_json_layer.get_bounds())

# 准备热力图数据
heat_data = df[['wgs_s_lat', 'wgs_s_lng']].values.tolist()

# 添加热力图
HeatMap(
    heat_data,
    radius=8,
    blur=10,
    max_zoom=1
).add_to(m)



# 保存为HTML文件
import os

# 确保 HTML 文件路径为绝对路径
output_html = os.path.abspath("嘉定区接单热力图.html")
m.save(output_html)

# 配置Selenium WebDriver（需要安装ChromeDriver）
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
service = Service(executable_path=r"C:\Users\28022\Desktop\chromedriver-win64\chromedriver-win64\chromedriver.exe")  # 替换为你的ChromeDriver路径
driver = webdriver.Chrome(service=service, options=chrome_options)

# 确保 Selenium 加载文件时使用绝对路径
driver.get(f"file://{output_html}")
time.sleep(5)  # 等待加载
png_output = "heat_map.png"
driver.save_screenshot(png_output)
driver.quit()

# 使用Pillow对图片进行美化
# 打开渲染的图片并转换为RGB模式
try:
    image = Image.open("heat_map.png").convert("RGB")
except FileNotFoundError:
    print("图片文件不存在，请检查路径！")
    exit()

draw = ImageDraw.Draw(image)

# 字体路径
font_path = "C:\\Windows\\Fonts\\SimHei.ttf"  # 替换为实际字体路径
try:
    font = ImageFont.truetype(font_path, 36)
except Exception as e:
    print(f"字体加载失败：{e}")
    exit()

# 添加标题
title = "嘉定区接单热力图"
# 获取文本边界框
text_bbox = draw.textbbox((0, 0), title, font=font)
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# 在图片顶部添加标题
draw.text(
    ((image.width - text_width) / 2, 20),  # 居中
    title,
    font=font,
    fill="black"
)

# 添加边框
border_color = (0, 128, 0)  # 深绿色
border_width = 10
image_with_border = Image.new("RGB", (image.width + 2 * border_width, image.height + 2 * border_width), border_color)
image_with_border.paste(image, (border_width, border_width))

# 保存美化后的图片
final_output = "heatmap1.png"
image_with_border.save(final_output,dpi=(500, 500))

print(f"美化图片已保存为：{final_output}")
