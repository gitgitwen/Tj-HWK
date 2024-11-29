clc; clear;
%% 准备
data = readtable('q2_fig.xlsx');
time_in_hours = data.N_i * 24;  % 将十进制时间转换为小时
time_in_minutes = mod(time_in_hours, 1) * 60;  % 计算分钟
time_in_hours = floor(time_in_hours);  % 获取小时部分
% 处理进位情况
for i = 1:length(time_in_hours)
    if time_in_minutes(i) >= 60
        time_in_hours(i) = time_in_hours(i) + floor(time_in_minutes(i) / 60);
        time_in_minutes(i) = mod(time_in_minutes(i), 60);
    end
end
%% 开始
% 创建时间字符串
time_labels = strcat(string(time_in_hours), ':', sprintf('%02d', round(time_in_minutes))); % 确保分钟格式为两位数
% 创建一个新的时间序列，以一小时为步长
time_series = datetime(0, 1, 1, 0, 0, 0):hours(1):datetime(0, 1, 1, 23, 0, 0);
time_labels_series = strcat(datestr(time_series, 'HH:MM'));
% 计算每个时间点的客流量
volume_series = zeros(length(time_labels_series), 1);
for i = 1:length(time_labels_series)
    if i <= length(time_labels)
        volume_series(i) = data.volume(i);
    end
end
% 将时间序列转换为数字表示，用于定位柱子的中间位置
time_numeric = datenum(time_series);
% 向右移动柱子位置，让柱子在两个时间点之间
bar_positions = time_numeric + (1/48);  % 1小时是1/24天，所以向右移动半小时即 1/48天
% 绘柱状图
figure;
bar(bar_positions, volume_series(1:length(time_series)), 0.8, 'FaceColor', [200/255, 191/255, 217/255]);  
set(gca, 'XTick', time_numeric, 'XTickLabel', time_labels_series, 'XTickLabelRotation', 90);  
xlabel('时间', 'FontSize', 20); 
ylabel('最大断面客流（人/h）', 'FontSize', 20); 
set(gca, 'FontSize', 12);  
grid on; 
datetick('x', 'HH:MM', 'keepticks'); % 使用日期格式化横轴显示
set(gca, 'FontSize', 18); % 调整图形的字体和大小
set(gcf, 'Position', [50, 50, 1750, 750]); % 设置图形窗口大小 
% 添加数值标签
for i = 1:length(volume_series)
    if volume_series(i) > 0  % 仅为大于0的柱子添加标签
        text(bar_positions(i), volume_series(i) + 5, num2str(volume_series(i)), 'HorizontalAlignment', 'center', 'FontSize', 18);
    end
end
