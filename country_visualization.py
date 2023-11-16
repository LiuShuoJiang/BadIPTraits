import json
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd


# Function to load data from JSON file
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


# Function to count visitors per country
def count_visitors(data):
    return {country: len(data[country]) for country in data}


# Function to create a bar chart
def plot_bar_chart(visitor_counts):
    sorted_counts = dict(sorted(visitor_counts.items(), key=lambda item: item[1], reverse=True))
    plt.figure(figsize=(15, 8))
    plt.bar(sorted_counts.keys(), sorted_counts.values())
    plt.xlabel('Country')
    plt.ylabel('Number of Visitors')
    plt.title('Number of Visitors by Country')
    plt.xticks(rotation=90)
    plt.show()


# Function to create a pie chart
def plot_pie_chart(visitor_counts):
    top_countries = dict(list(sorted(visitor_counts.items(), key=lambda item: item[1], reverse=True))[:10])
    plt.figure(figsize=(10, 10))
    plt.pie(top_countries.values(), labels=top_countries.keys(), autopct='%1.1f%%')
    plt.title('Top 10 Countries by Visitor Share')
    plt.show()


def plot_geo_chart(data):
    visitor_counts = {country: len(ips) for country, ips in data.items()}

    world_shapefile_path = 'ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp'
    world = gpd.read_file(world_shapefile_path)

    # Use 'ADMIN' as the country name column
    world = world.set_index('ADMIN').join(pd.DataFrame.from_dict(visitor_counts, orient='index', columns=['visitors']))

    # Ensure missing values are handled
    world['visitors'] = world['visitors'].fillna(0)

    # Plot
    world.plot(column='visitors', cmap='OrRd', legend=True, figsize=(15, 10),
               missing_kwds={'color': 'lightgrey'})
    plt.title('World Map of Website Visitors')
    plt.show()


# Main execution
if __name__ == "__main__":
    file_path = './country.json'  # Update with the path to your JSON file
    data = load_data(file_path)
    visitor_counts = count_visitors(data)
    plot_bar_chart(visitor_counts)
    plot_pie_chart(visitor_counts)
    plot_geo_chart(data)
