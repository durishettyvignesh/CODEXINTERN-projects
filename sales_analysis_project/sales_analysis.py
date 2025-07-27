import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns



# Load file
df = pd.read_csv( 'sales_data.csv' )



# Show first rows
print( "🔍 First 5 rows of the data:" )

print( df.head() )



# Average of sales
avg = df[ 'Sales' ].mean()

print( "\n📊 Average Sales: ₹" , round( avg , 2 ) )



# Bar chart - avg sale for each category
plt.figure( figsize = ( 8 , 5 ) )

grp = df.groupby( 'Category' )[ 'Sales' ].mean()

grp = grp.sort_values()

grp.plot( kind = 'bar' , color = 'skyblue' )

plt.title( "Average Sales per Category" )

plt.xlabel( "Category" )

plt.ylabel( "Average Sales" )

plt.xticks( rotation = 45 )

plt.tight_layout()

plt.show()



# Scatter plot - sale vs profit
plt.figure( figsize = ( 8 , 5 ) )

plt.scatter( df[ 'Sales' ] , df[ 'Profit' ] , color = 'green' , alpha = 0.6 )

plt.title( "Sales vs Profit" )

plt.xlabel( "Sales (₹)" )

plt.ylabel( "Profit (₹)" )

plt.grid( True )

plt.tight_layout()

plt.show()



# Heatmap for correlation
plt.figure( figsize = ( 6 , 4 ) )

corr = df.corr( numeric_only = True )

sns.heatmap( corr , annot = True , cmap = 'coolwarm' , linewidths = 0.5 )

plt.title( "Correlation Heatmap" )

plt.tight_layout()

plt.show()



# Save new file
df.to_csv( 'processed_sales_data.csv' , index = False )

print( "\n✅ Processed data saved to 'processed_sales_data.csv'." )
