clc;
clear;
data = readtable('question_4_v.xlsx');
time_20s = datetime(data.("time_20s_"), 'InputFormat', 'yyyy-MM-dd HH:mm:ss'); 
v_20s = data.("x20s"); 
time_5min = datetime(data.("time_5min_"), 'InputFormat', 'yyyy-MM-dd HH:mm:ss.SSS'); 
v_5min = data.("x5min");
time_15min = datetime(data.("time_15min_"), 'InputFormat', 'yyyy-MM-dd HH:mm:ss'); 
v_15min = data.("x15min"); 
figure;
scatter(time_20s, v_20s, 6, 'b', 'filled'); 
hold on;
plot(time_5min, v_5min, 'r-o', 'LineWidth', 2, 'MarkerSize', 2); 
plot(time_15min, v_15min, 'g-s', 'LineWidth', 2, 'MarkerSize', 2); 
legend({'20秒周期散点', '5分钟周期曲线', '15分钟周期曲线'}, 'FontSize', 12, 'Location', 'northwest');
xlabel('时间 (时:分:秒)', 'Interpreter', 'latex', 'FontSize', 14);
ylabel('速度 (v)', 'Interpreter', 'latex', 'FontSize', 14);
ax = gca;
datetick('x','HH:MM:SS','keepticks'); 
ax.XTickLabelRotation = 45; 
ax.FontSize = 12; 
ax.LineWidth = 1.5; 
grid on; 
set(gca, 'GridLineStyle', '--', 'GridColor', 'k', 'GridAlpha', 0.2); 
set(gca, 'Box', 'on');
set(gcf, 'Position', [100, 100, 1200, 800]);
set(gca, 'FontWeight', 'bold');
hold off;
