import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

class PlotDrawer:
    def __init__(self, filepath):
        self.filepath = filepath

    def draw_plots(self):
        self.df = pd.read_json(self.filepath)

        os.makedirs('plots', exist_ok=True)
        plot_paths = []

        # Comparing of true corners and Predicted corners
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data=self.df, x='gt_corners', y='rb_corners', color='red', label='Predicted')
        plt.plot([self.df['gt_corners'].min(), self.df['gt_corners'].max()], [self.df['gt_corners'].min(), self.df['gt_corners'].max()], 'k--', label='Ideal')
        plt.title('True vs. Predicted Corners')
        plt.xlabel('True Number of Corners')
        plt.ylabel('Predicted Number of Corners')
        plt.legend()
        plt.tight_layout()
        comparison_plot_path = 'plots/true_vs_predicted.png'
        plt.savefig(comparison_plot_path)
        plt.close()
        plot_paths.append(comparison_plot_path)

        # linear graph for floor mean ceiling mean
        plt.figure(figsize=(8, 5))
        sns.lineplot(x='gt_corners', y='floor_mean', data=self.df, color='blue', label='Floor Mean')
        sns.lineplot(x='gt_corners', y='ceiling_mean', data=self.df, color='green', label='Ceiling Mean')
        plt.title('Comparison of Ground Truth Corners to Floor and Ceiling Means')
        plt.xlabel('Ground Truth Corners')
        plt.ylabel('Mean Deviation in Degrees')
        plt.legend()
        plt.tight_layout()
        floor_ceiling_mean_plot = 'plots/floor_ceiling_mean_comparison_line.png'
        plt.savefig(floor_ceiling_mean_plot)
        plt.close()
        plot_paths.append(floor_ceiling_mean_plot)

        #Scatterplot for Floor mean Ceiling mean
        plt.figure(figsize=(8, 10))
        sns.scatterplot(x='gt_corners', y='floor_mean', data=self.df, color='blue', label='Floor Mean')
        sns.scatterplot(x='gt_corners', y='ceiling_mean', data=self.df, color='green', label='Ceiling Mean')
        plt.title('Comparison of Ground Truth Corners to Floor and Ceiling Means')
        plt.xlabel('Ground Truth Corners')
        plt.ylabel('Mean Deviation in Degrees')
        plt.legend()
        plt.tight_layout()
        floor_ceiling_mean_plot = 'plots/floor_ceiling_mean_comparison.png'
        plt.savefig(floor_ceiling_mean_plot)
        plt.close()
        plot_paths.append(floor_ceiling_mean_plot)

        #Histogram of deviation
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x='mean', kde=True, color='blue', label='Mean Deviation')
        plt.title('Histogram of Mean Deviations')
        plt.xlabel('Deviation in Degrees')
        plt.ylabel('Frequency')
        plt.legend()
        plt.tight_layout()
        histogram_plot = 'plots/deviation_histogram.png'
        plt.savefig(histogram_plot)
        plt.close()
        plot_paths.append(histogram_plot)

        # Box plot max min deviation
        melted_df = self.df.melt(id_vars=['gt_corners'], value_vars=['max', 'min'], var_name='Statistic', value_name='Deviation')
        plt.figure(figsize=(8, 10))
        sns.boxplot(x='Statistic', y='Deviation', data=melted_df)
        plt.title('Box Plot of Max and Min Deviations')
        plt.xlabel('Statistic')
        plt.ylabel('Deviation in Degrees')
        plt.tight_layout()
        boxplot_path = 'plots/max_min_boxplot.png'
        plt.savefig(boxplot_path)
        plt.close()
        plot_paths.append(boxplot_path)

        return plot_paths


# def main():
#     draw = PlotDrawer("deviation.json")
#     plot_paths = draw.draw_plots()

#     for path in plot_paths:
#         print(path)

# if __name__ == '__main__':
#     main()


# df = pd.read_json("deviation.json")
# # print(df.describe().T)
# print(df.head(10).T)





