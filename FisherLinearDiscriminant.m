%{
FisherLinearDiscriminant.m

This MATLAB script generates two parallel noisy lines in 3D space that  
share the same principal direction of variance but are separated in a 
direction orthogonal to that variance. It applies Principal Component 
Analysis (PCA) and Fisher s Linear Discriminant (FLD) to project the 
data into one dimension. The visualization consists of three panels: 
the left shows the 3D structure of the two classes, while the right 
side displays their one-dimensional projections using PCA and FLD. 

PCA fails to separate the classes due to its focus on maximizing overall 
variance, which is aligned for both groups. In contrast, FLD uses 
label information to find a projection that maximizes class separation 
and thus produces a clear division between the two groups.

By Juan B. Gutiérrez, Professor of Mathematics
University of Texas at San Antonio.

License: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
%}

% Generate two parallel lines in 3D
rng('default');
rng(0);
n = 50;
line1 = [linspace(0, 10, n)', ones(n,1), ones(n,1)];
line2 = [linspace(0, 10, n)', ones(n,1)*3, ones(n,1)*3];

% Add some Gaussian noise
line1 = line1 + 0.1*randn(n,3);
line2 = line2 + 0.1*randn(n,3);

% Combine data and labels
X = [line1; line2];
y = [zeros(n,1); ones(n,1)];

% Perform PCA
X_centered = X - mean(X);
[coeff, ~, ~] = pca(X);
X_pca1D = X_centered * coeff(:,1);

% Perform Fisher's Linear Discriminant
mu1 = mean(X(y==0,:),1);
mu2 = mean(X(y==1,:),1);
S1 = cov(X(y==0,:));
S2 = cov(X(y==1,:));
Sw = S1 + S2;
w_fld = Sw \ (mu2 - mu1)';
w_fld = w_fld / norm(w_fld);

X_fld1D = (X - mean(X,1)) * w_fld;

% Plot
figure('Position', [100, 100, 1200, 600]);

% 3D Plot
subplot('Position', [0.05, 0.35, 0.4, 0.55]);
h1 = plot3(line1(:,1), line1(:,2), line1(:,3), 'o'); hold on;
h2 = plot3(line2(:,1), line2(:,2), line2(:,3), 'x');
xlabel('X'); ylabel('Y'); zlabel('Z');
title('3D Parallel Lines');
grid on; view(3);
legend([h1, h2], {'Class 0', 'Class 1'});

% Explanatory Text Below 3D Plot
annotation('textbox', [0.05, 0.05, 0.4, 0.2], 'String', 'This MATLAB script generates two parallel noisy lines in 3D space that share the same principal direction of variance but are separated in a direction orthogonal to that variance. It applies Principal Component Analysis (PCA) and Fisher''s Linear Discriminant (FLD) to project the data into one dimension. PCA fails to separate the classes due to its focus on maximizing overall variance, which is aligned for both groups. In contrast, FLD uses label information to find a projection that maximizes class separation and thus produces a clear division between the two groups.', 'EdgeColor', 'none', 'FontSize', 12, 'Interpreter', 'none', 'FitBoxToText', 'off', 'HorizontalAlignment', 'left');

% PCA Projection
subplot('Position', [0.55, 0.55, 0.4, 0.35]);
scatter(X_pca1D(y==0), zeros(n,1), 'o'); hold on;
scatter(X_pca1D(y==1), zeros(n,1), 'x');
ylim([-1, 1]); yticks([]);  % Remove y-axis ticks to emphasize 1D
title('PCA Projection to 1D');
xlabel('Projection value');
legend({'Class 0','Class 1'});

% FLD Projection
subplot('Position', [0.55, 0.1, 0.4, 0.35]);
scatter(X_fld1D(y==0), zeros(n,1), 'o'); hold on;
scatter(X_fld1D(y==1), zeros(n,1), 'x');
ylim([-1, 1]); yticks([]);  % Remove y-axis ticks to emphasize 1D
title('Fisher''s LDA Projection to 1D');
xlabel('Projection value');
legend({'Class 0','Class 1'});
