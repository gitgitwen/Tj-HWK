%% 准备
OD = readmatrix('q2_OD.mat.xlsx'); % 读入矩阵
[m, n] = size(OD); % 计算矩阵大小
if m ~= n
    error('OD矩阵必须是方阵');
end
if m ~= 18
    warning('OD矩阵的大小不是18x18，请确认数据是否正确。');
end
stationNames = cell(1, m); % 定义站点名称，以数字为例
for i = 1:m
    stationNames{i} = num2str(i); % 将站点名称定义为数字字符串
end
sectionFlow = zeros(1, m-1); % 初始化断面客流
%% 开始
% 计算每一断面客流
for n = 1:(m-1)
    % 直接流量：从第k站到第k+1站及其后续站点的OD流量之和
    directFlow = sum(OD(n, (n+1):m));
    % 上游流量：
    % 如果k不是第一个站点，则需要加上所有前面站点到第k+1站及其后续站点的OD流量之和
    if n == 1
        upstreamFlow = 0; % 当k=1时，没有前面的站点
    else
        upstreamFlow = sum(sum(OD(1:(n-1), (n+1):m)));
    end
    totalFlow = directFlow + upstreamFlow; % 总断面客流
    sectionFlow(n) = round(totalFlow); % 四舍五入
end
format long g;
% 显示断面客流结果
fprintf('断面客流结果：\n');
for n = 1:(m-1)
    fromStation = stationNames{n};
    toStation = stationNames{n+1};
    fprintf('%s~%s：%d\n', fromStation, toStation, sectionFlow(n));
end
%% 绘制断面客流量分布图
x = 1:m; % 从1到18
y = [sectionFlow, 0]; % 将最后一站的流量设为0，以便画到第18站
figure('Color', 'w'); % 设置背景为白色
specifiedColor =  [125, 164, 148] / 255;
hold on;
for n = 1:(m-1)
    % 画水平线段连接相邻的数字
    plot([x(n), x(n+1)], [y(n), y(n)], 'LineWidth', 2, 'Color', specifiedColor); % 水平线
    % 仅在不是最后一个点时绘制竖直线段
    if n < m - 1
        plot([x(n+1), x(n+1)], [y(n), y(n+1)], 'LineWidth', 2, 'Color', specifiedColor); % 竖直线
    end
end
xticks(x); 
xticklabels(x); 
xtickangle(0);

ylabel('高峰流量（人/1h）', 'FontSize', 12, 'FontWeight', 'bold'); % 设置y轴
xlabel('站点编号', 'FontSize', 12, 'FontWeight', 'bold'); % 设置x轴
grid on; grid minor;
set(gca, 'FontSize', 15, 'FontWeight', 'bold'); % 调整图形的字体和大小
set(gcf, 'Position', [50, 50, 1750, 750]); % 设置图形窗口大小

% % 显示数据标签
% for n = 1:m
%     if n < m
%         text(x(n), y(n) + max(y) * 0.01, num2str(y(n)), ...
%             'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom', ...
%             'FontSize', 15);
%     else
%         text(x(n), 0 + max(y) * 0.01, num2str(0), ...
%             'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom', ...
%             'FontSize', 15);
%     end
% end
legend('10:30~11:30', 'Location', 'northeast'); % 添加图例
hold off;
