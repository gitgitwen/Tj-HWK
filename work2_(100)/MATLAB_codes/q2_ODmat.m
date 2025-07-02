clc; clear;

%% 准备
epsilon = 0.01;  % 设置收敛阈值
x_k = triu(ones(18));  %创建初始OD矩阵（大小自己设置） 
for i = 1:18
    x_k(i, i) = 0; 
end 
B = [63,0,9,13,25,7,0,11,36,52,12,95,46,53,8,17,9,0]; % 上行乘客数据
A = [0,2,5,7,15,13,3,14,16,15,4,22,88,58,17,21,85,71]; % 下行乘客数据
decision = false; % 收敛条件
iteration_count = 0; 
tic;
%% 开始循环
while ~decision
    iteration_count = iteration_count + 1; 
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
elapsed_time = toc; 
% 输出最终的 OD 矩阵
disp('最终的 OD 矩阵:');
disp(round(x_k)); 
% 输出迭代次数和所用时间
fprintf('迭代次数: %d\n', iteration_count);
fprintf('所用时间: %.4f 秒\n', elapsed_time);
