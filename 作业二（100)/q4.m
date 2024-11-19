clc; clear;
%% 准备
data1 = readtable('q2_fig.xlsx');  % 从Excel文件中读取数据
data2 = readtable('q4.xlsx');
time_in_hours1 = data1.N_i * 24;  % 将十进制时间转换为小时
time_in_minutes = mod(time_in_hours1, 1) * 60;  % 计算分钟
time_in_hours1 = floor(time_in_hours1);  % 获取小时部分

% 处理进位情况
for i = 1:length(time_in_hours1)
    if time_in_minutes(i) >= 60
        time_in_hours1(i) = time_in_hours1(i) + floor(time_in_minutes(i) / 60);
        time_in_minutes(i) = mod(time_in_minutes(i), 60);
    end
end

% 创建时间字符串
time_labels = strcat(string(time_in_hours1), ':', sprintf('%02d', round(time_in_minutes))); % 确保分钟格式为两位数

% 创建时间序列
time_series = datetime(0, 1, 1, 0, 0, 0):hours(1):datetime(0, 1, 1, 24, 0, 0); % 0:00 到 24:00
volume_series1 = data1.volume;  % 提取客流量数据
volume_series2 = data2.volume;

% 确保 volume_series2 的长度与 time_series 相同
if length(volume_series2) < length(time_series)
    volume_series2(end + 1:length(time_series)) = 0; % 填充剩余部分为0
end

%% 绘制断面客流量分布图
figure('Color', 'w'); % 设置背景为白色
specifiedColor1 = [193, 110, 113] / 255; % 指定颜色
specifiedColor2 = [125, 164, 148] / 255; % 指定颜色
hold on;

% 向量化绘制 volume_series1
x_values1 = []; % 存储x坐标
y_values1 = []; % 存储y坐标

for n = 1:(length(volume_series1)-1)
    if volume_series1(n) > 0
        % 水平线段的x和y坐标
        x_values1 = [x_values1, time_series(n), time_series(n+1)];
        y_values1 = [y_values1, volume_series1(n), volume_series1(n)];
    end
end
plot(x_values1, y_values1, 'LineWidth', 2, 'Color', specifiedColor2); % 绘制所有水平线

% 向量化绘制 volume_series2
x_values2 = []; % 存储x坐标
y_values2 = []; % 存储y坐标

for n = 1:(length(volume_series2)-1)
    if volume_series2(n) > 0
        % 水平线段的x和y坐标
        x_values2 = [x_values2, time_series(n), time_series(n+1)];
        y_values2 = [y_values2, volume_series2(n), volume_series2(n)];
    end
end
plot(x_values2, y_values2, 'LineWidth', 2, 'Color', specifiedColor1); % 绘制所有水平线

% 设置x轴和y轴
xticks(time_series); 
xticklabels(datestr(time_series, 'HH:MM')); % 只显示小时和分钟
xtickangle(30); % 设置x轴标签角度

ylabel('最大断面客流 (人/h)', 'FontSize', 12, 'FontWeight', 'bold'); % 设置左侧y轴
xlabel('时间/h', 'FontSize', 12, 'FontWeight', 'bold'); % 设置x轴

% 添加右边的竖坐标标签
yyaxis right; % 切换到右边的Y轴
ylabel('计划运输能力 (人/h)', 'FontSize', 12, 'FontWeight', 'bold'); % 设置右侧y轴标签

% 设置右边y轴属性
set(gca, 'YColor', 'k'); % 设置右边y轴的颜色为黑色
yticks(0:50:500); % 设置y轴的刻度从0到500，步长为50
ylim([0 500]); % 设置右边y轴的范围

grid on; grid minor; 
set(gca, 'FontSize', 10, 'FontWeight', 'bold'); % 调整图形的字体和大小
set(gcf, 'Position', [100, 100, 1200, 600]); % 设置图形窗口大小

% 添加图例，确保颜色与线相对应
legend({'最大断面客流', '计划运输能力'}, 'Location', 'northeast'); % 添加图例

hold off;
