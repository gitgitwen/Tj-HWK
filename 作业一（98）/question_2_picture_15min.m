clc;
clear;
opts = spreadsheetImportOptions("NumVariables", 4);
opts.Sheet = "线圈数据15min";
opts.DataRange = "A2:D288";
opts.VariableNames = ["Var1", "Var2", "Var3", "FINT_VOLUMEveh15min"];
opts.SelectedVariableNames = "FINT_VOLUMEveh15min";
opts.VariableTypes = ["char", "char", "char", "double"];
opts = setvaropts(opts, ["Var1", "Var2", "Var3"], "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["Var1", "Var2", "Var3"], "EmptyFieldRule", "auto");
tbl = readtable("C:\Users\28022\Desktop\作业一数据(不宜改动).xlsx", opts, "UseExcel", false);
q = tbl.FINT_VOLUMEveh15min;
clear opts tbl
opts = spreadsheetImportOptions("NumVariables", 5);
opts.Sheet = "线圈数据15min";
opts.DataRange = "A2:E288";
opts.VariableNames = ["Var1", "Var2", "Var3", "Var4", "FINT_SPEEDkmh"];
opts.SelectedVariableNames = "FINT_SPEEDkmh";
opts.VariableTypes = ["char", "char", "char", "char", "double"];
opts = setvaropts(opts, ["Var1", "Var2", "Var3", "Var4"], "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["Var1", "Var2", "Var3", "Var4"], "EmptyFieldRule", "auto");
tbl = readtable("C:\Users\28022\Desktop\作业一数据(不宜改动).xlsx", opts, "UseExcel", false);
v = tbl.FINT_SPEEDkmh;
clear opts tbl
opts = spreadsheetImportOptions("NumVariables", 6);
opts.Sheet = "线圈数据15min";
opts.DataRange = "A2:F288";
opts.VariableNames = ["Var1", "Var2", "Var3", "Var4", "Var5", "FINT_OCCUPY"];
opts.SelectedVariableNames = "FINT_OCCUPY";
opts.VariableTypes = ["char", "char", "char", "char", "char", "double"];
opts = setvaropts(opts, ["Var1", "Var2", "Var3", "Var4", "Var5"], "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["Var1", "Var2", "Var3", "Var4", "Var5"], "EmptyFieldRule", "auto");
tbl = readtable("C:\Users\28022\Desktop\作业一数据(不宜改动).xlsx", opts, "UseExcel", false);
o = tbl.FINT_OCCUPY;
clear opts tbl
%绘制散点图
scatterSize = 15; % 设置散点大小为10，较小的点

% 绘制“o-v”散点图
figure; % 单独创建图窗
scatter(o, v, scatterSize, 'b', 'filled', 'MarkerEdgeColor', 'k'); % 绘制散点图
title('Scatter plot of o vs v', 'FontSize', 14, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 设置标题
xlabel('o', 'FontSize', 12, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 设置 x 轴标签
ylabel('v', 'FontSize', 12, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 设置 y 轴标签
grid on; % 打开网格线
set(gca, 'GridLineStyle', '--', 'LineWidth', 1.2); % 设置网格为虚线和线宽
box on; % 打开轴线框
set(gca, 'FontSize', 12, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 统一设置字体风格和大小
set(gcf, 'Color', 'w'); % 设置背景为白色

% 绘制“o-q”散点图
figure; % 单独创建图窗
scatter(o, q, scatterSize, 'r', 'filled', 'MarkerEdgeColor', 'k'); % 绘制散点图
title('Scatter plot of o vs q', 'FontSize', 14, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 设置标题
xlabel('o', 'FontSize', 12, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 设置 x 轴标签
ylabel('q', 'FontSize', 12, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 设置 y 轴标签
grid on; % 打开网格线
set(gca, 'GridLineStyle', '--', 'LineWidth', 1.2); % 设置网格为虚线和线宽
box on; % 打开轴线框
set(gca, 'FontSize', 12, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 统一设置字体风格和大小
set(gcf, 'Color', 'w'); % 设置背景为白色

% 绘制“v-q”散点图
figure; % 单独创建图窗
scatter(q, v, scatterSize, 'g', 'filled', 'MarkerEdgeColor', 'k'); % 绘制散点图
title('Scatter plot of v vs q', 'FontSize', 14, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 设置标题
ylabel('v', 'FontSize', 12, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 设置 x 轴标签
xlabel('q', 'FontSize', 12, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 设置 y 轴标签
grid on; % 打开网格线
set(gca, 'GridLineStyle', '--', 'LineWidth', 1.2); % 设置网格为虚线和线宽
box on; % 打开轴线框
set(gca, 'FontSize', 12, 'FontWeight', 'bold', 'FontName', 'Times New Roman'); % 统一设置字体风格和大小
set(gcf, 'Color', 'w'); % 设置背景为白色
