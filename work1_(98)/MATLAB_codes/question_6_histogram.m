clc;
clear;
opts = spreadsheetImportOptions("NumVariables", 8);
% 指定工作表
opts.Sheet = "线圈数据15min";
% 指定列名称和类型
opts.VariableNames = ["Var1", "Var2", "Var3", "Var4", "Var5", "Var6", "Var7", "VEHICLELENGTH"];
opts.SelectedVariableNames = "VEHICLELENGTH";
opts.VariableTypes = ["char", "char", "char", "char", "char", "char", "char", "double"];
% 指定变量属性
opts = setvaropts(opts, ["Var1", "Var2", "Var3", "Var4", "Var5", "Var6", "Var7"], "WhitespaceRule", "preserve");
opts = setvaropts(opts, ["Var1", "Var2", "Var3", "Var4", "Var5", "Var6", "Var7"], "EmptyFieldRule", "auto");
% 导入数据
tbl = table;
ranges = ["A3:H4", "A21:H288"];
for idx = 1:length(ranges)
    opts.DataRange = ranges(idx);
    tb = readtable("ans_1.xlsx", opts, "UseExcel", false);
    tbl = [tbl; tb]; %#ok<AGROW>
end
VEHICLELENGTH = tbl.VEHICLELENGTH;
clear idx opts ranges tb tbl
% 计算数据的均值和标准差，用于拟合正态分布
mu = mean(VEHICLELENGTH);
sigma = std(VEHICLELENGTH);
% 绘制直方图
figure;
histogram(VEHICLELENGTH, 'Normalization', 'pdf', 'BinMethod', 'fd'); % 使用 Freedman-Diaconis 方法选择合理的分箱数
% 在直方图上叠加正态分布的概率密度函数
hold on;
x = min(VEHICLELENGTH):0.01:max(VEHICLELENGTH);  % x轴范围
y = normpdf(x, mu, sigma);  % 计算正态分布的概率密度
plot(x, y, 'r-', 'LineWidth', 1.5);  % 绘制概率密度函数，红色实线
% 设置横纵坐标标签
xlabel('Average Effective Vehicle Length(m)', 'Interpreter', 'latex', 'FontSize', 14);  % 横坐标
ylabel('Probability Density', 'Interpreter', 'latex', 'FontSize', 14);  % 纵坐标
grid on;  % 打开网格线
set(gca, 'FontName', 'Times New Roman', 'FontSize', 12);  % 设置字体
set(gcf, 'Color', 'w');  % 设置背景为白色
box on;  % 加入边框
hold off;
