clc;
clear;
filename='gather_15min.xlsx';  
opts=detectImportOptions(filename); 
data=readtable(filename, opts);  
FINT_VOLUME=data.FINT_VOLUME(2:end);  % 从第二行开始的FINT_VOLUME列
FINT_SPEED=data.FINT_SPEED(2:end);  % 从第二行开始的FINT_SPEED列
second=data.false_second(2:end);  % 从第二行开始的second列
% 定义组大小（5min）
size=45;
% 计算总组数
groups=floor(length(FINT_VOLUME)/size);
% 初始化新表格
new_data=table('Size',[groups, 3],...
                'VariableTypes',{'double','double','double'}, ...
                'VariableNames',{'FINT_VOLUME','FINT_SPEED','FINT_OCCUPY'});
for i = 1:groups
    % 第1列: 每组FINT_VOLUME的和
    start=(i-1)*size + 1;
    end_i=min(i*size,length(FINT_VOLUME));
    new_data.FINT_VOLUME(i)=sum(FINT_VOLUME(start:end_i));
    % 第2列: 每组FINT_SPEED的平均
    new_data.FINT_SPEED(i)=mean(FINT_SPEED(start:end_i));
    % 第3列: 每组second的合计除以900
    new_data.FINT_OCCUPY(i)=sum(second(start:end_i))/900;
end
disp(new_data);

