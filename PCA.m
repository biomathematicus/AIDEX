% PCA - Create two random sets

M1 = rand(10,3)+2;
M2 = -rand(10,3)+2;
M = [M1; M2]
figure(1); hold off
plot3(M(1:10,1),M(1:10,2),M(1:10,3), 'r*')
hold on
plot3(M(11:20,1),M(11:20,2),M(11:20,3), 'b*')
grid on

% Subtract the mean
N = M - mean(M);
% Compute scatter (~covariance)
S = N'*N;
% Compute eigenvectors & eigenvalues
[V,D] = eig(S);

figure(2); hold off
plot(M1*V(:,3), M1*V(:,2), 'r*')
hold on
plot(M2*V(:,3), M2*V(:,2), 'b*')

% Plot Pareto of eigenvalues
eigenvalues = diag(D);
[sorted_vals, idx] = sort(eigenvalues, 'descend');
normalized_vals = sorted_vals / sum(sorted_vals);
cumulative_vals = cumsum(normalized_vals);

figure(3); hold off
bar(normalized_vals, 'FaceColor', [0.2 0.2 0.5])
hold on
plot(cumulative_vals, '-o', 'Color', [0.8 0 0], 'LineWidth', 2)
grid on
title('Pareto Plot of PCA Eigenvalues')
xlabel('Principal Component')
ylabel('Variance Explained')
legend('Individual', 'Cumulative', 'Location', 'best')
