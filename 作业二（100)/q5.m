clc; clear;

%% 准备
epsilon = 0.0001;  % 设置收敛阈值
x_k = triu(ones(18));  %创建初始OD矩阵（大小自己设置） 
for i = 1:18
    x_k(i, i) = 0; 
end 
B = [625,33,150,98,304,64,8,93,401,488,72,902,423,355,282,43,69,0]; % 上行乘客数据
A = [0,50,29,51,119,162,8,107,209,203,27,243,740,641,267,146,412,996]; % 下行乘客数据
decision = false; % 收敛条件

%% 开始循环
while ~decision
    
    % 按行更新
    for i = 1:size(x_k, 1) - 1
        pb_i_k = sum(x_k(i,:));
        if pb_i_k > 0
            for j = i + 1:size(x_k, 2) 
                x_k(i,j) = x_k(i,j) * (B(i) / pb_i_k);
            end
        end
    end
    % 按列更新
    for j = size(x_k, 2):-1:2
        pa_j_k = sum(x_k(:,j));
        if pa_j_k > 0
            for i = 1:j - 1 
                x_k(i,j) = x_k(i,j) * (A(j) / pa_j_k);
            end
        end
    end
    % 更新完成，计算缩放比例
    validation = ones(2, size(x_k, 1));
    for i = 1:size(x_k, 1)
        pb_i_k_o = sum(x_k(i,:));
        if pb_i_k_o > 0
            validation(1,i) = B(i) / pb_i_k_o;
        else
            validation(1,i) = 1; 
        end
    end
    for j = size(x_k, 2):-1:1
        pa_j_k_o = sum(x_k(:,j));
        if pa_j_k_o > 0
            validation(2,j) = A(j) / pa_j_k_o;
        else
            validation(2,j) = 1; 
        end
    end
    % 检查收敛条件
    decision = true; 
    for i = 1:2
        for j = 1:size(validation, 2)
            current = validation(i,j);
            if current < (1 - epsilon) || current > (1 + epsilon)
                decision = false;
                break;
            end
        end
        if ~decision
            break; 
        end
    end
end

% 假设 cum_dist 是一个 18x1 的向量，包含每个车站到第一个车站的累计距离
cum_dist = [0.000,0.513,1.117,1.625,2.358,2.793,3.304,3.550,3.918,4.123,4.447,4.654,5.228,5.566,5.983,6.286,6.797,7.836]; % 请将 d1 到 d18 替换为实际距离值

n = 18; % 车站数量
D = zeros(n, n); % 初始化 18x18 的距离矩阵为零

for i = 1:n
    for j = (i+1):n
        D(i, j) = cum_dist(j) - cum_dist(i);
    end
end

%计算PPK
PPK = round(sum(sum(D.*x_k)));
disp(['PPK:' , num2str(PPK)]);

%计算客运总量
Q = round(sum(sum(x_k)));
disp(['Q:',num2str(Q)]);

%计算客运里程
SK = 60 * sum(sum(D));
disp(['SK:',num2str(SK)]);
