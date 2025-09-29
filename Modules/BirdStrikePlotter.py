import pandas as pd
import hvplot.pandas
import holoviews as hv

class BirdStrikePlotter:
    def __init__(self, df):
        self.df = df
        self.df['month'] = self.df['flight_date'].dt.month
        self.df['year'] = self.df['flight_date'].dt.year
    
    def create_time_series_plot(self):
        time_series = self.df.groupby('flight_date').size().reset_index(name='count')
        return time_series.hvplot.line(
            x='flight_date', 
            y='count', 
            title='Bird Strikes Over Time', 
            xlabel='Flight Date',
            ylabel='Bird Strike Count',
            width=800, 
            height=400
        ).opts(tools=['hover'])
    
    def create_altitude_scatter_plot(self):
        return self.df.hvplot.scatter(
            x='altitude', 
            y='number_struck_actual', 
            title='Altitude vs. Number of Birds Struck', 
            xlabel='Altitude',
            ylabel='Number of birds struck',
            width=600, 
            height=400,
            color='wildlife_size',
            size=8,
            alpha=0.6
        ).opts(tools=['hover'])
    
    def create_heatmap(self):
        return self.df.groupby(['year', 'month']).size().unstack().hvplot.heatmap(
            title='Bird Strikes by month and year',
            width=800,
            height=400,
            cmap='YlOrRd',
            xlabel='Month',
            ylabel='Year'
        ).opts(tools=['hover'])
    
    def create_altitude_boxplot(self):
        return self.df.hvplot.box(
            y='altitude',
            by='wildlife_size',
            title='Altitude Distribution by Wildlife Size',
            xlabel='Wildlife Sizes',
            ylabel='Altitude',
            width=600,
            height=400
        ).opts(tools=['hover'])
    
    def create_dashboard(self):
        return (self.create_time_series_plot() + self.create_altitude_scatter_plot() + 
                self.create_heatmap() + self.create_altitude_boxplot()).cols(2)

