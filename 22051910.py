#Data Source Link : https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales
#Github Link : https://github.com/harighanapuram1329/dhv-assignment.git

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('supermarket_sales - Sheet1.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Set up Seaborn style
sns.set(style = "whitegrid")

# Custom color palettes
city_palette = "Set2"
product_palette = "viridis"
payment_palette = "pastel"
lineplot_color = "skyblue"

# Create a sales dashboard using Seaborn
fig , axs = plt.subplots(2 , 3 , figsize = (14 , 8))
fig.suptitle('Supermarket Sales Analysis' , fontsize = 16 ,
             fontweight = 'bold')

# Sales by City
sns.countplot(x = 'City' , hue = 'Customer type' , data = df ,
              ax = axs[0 , 0] , palette = city_palette)
axs[0 , 0].set_title('Count of Customers by City and Customer Type' ,
                     fontweight = 'bold')
axs[0 , 0].set_xlabel('City')
axs[0 , 0].set_ylabel('Count')
axs[0 , 0].legend(title = 'Customer Type')

# Sales by Product line
sns.countplot(x = 'Product line' , data = df ,
              palette = product_palette , ax = axs[0 , 1])
axs[0 , 1].set_title('Sales by Product Line' ,
                     fontweight = 'bold')
axs[0 , 1].set_xlabel('Product Line')
axs[0 , 1].set_ylabel('Count')
axs[0 , 1].set_xticklabels(axs[0 , 1].get_xticklabels() ,
                           rotation = 45)

# Total sales over time
sns.lineplot(x = 'Date' , y = 'Total' , data = df , marker = 'o' ,
             color = lineplot_color , ax = axs[0 , 2])
axs[0 , 2].set_title('Total Sales Over Time' , fontweight = 'bold')
axs[0 , 2].set_xlabel('Date')
axs[0 , 2].set_ylabel('Total Sales')
axs[0 , 2].set_xticklabels(axs[0 , 2].get_xticklabels() , rotation = 45)

# Payment method distribution
sns.countplot(x = 'Payment' , data = df , palette = payment_palette ,
              ax = axs[1 , 0])
axs[1 , 0].set_title('Payment Method Distribution' ,
                     fontweight = 'bold')
axs[1 , 0].set_xlabel('Payment Method')
axs[1 , 0].set_ylabel('Count')

# Additional text description grid
text = "1. More membership customers than regular consumers are \n" \
       "found in Yongana City. The Naypyitaw exclusively serves regular \n" \
       "consumers; it does not have any membership clients.\n" \
       "2. Supermarket sales of health and beauty products are high.\n" \
       "3. The supermarket's sales are declining each month.\n" \
       "4. The supermarket has a lot of eWallet payment options."

axs[1 , 1].text(0 , 0.5 , text , ha = 'left' , va = 'center' , fontsize = 12 ,
                multialignment = 'left' , color = 'darkred')
axs[1 , 1].axis('off')

# Additional text description grid
text = "Student name: Hari Prasad Ghanapuram \n" \
       "Student ID: 22051910"

axs[1 , 2].text(0 , 0.5 , text , ha = 'left' , va = 'center' , fontsize = 12 ,
                multialignment = 'left' , fontweight = 'bold' , color = 'darkblue')
# Empty subplot for layout
axs[1 , 2].axis('off')

plt.tight_layout(rect = [0 , 0 , 1 , 0.96])
plt.savefig('22051910.png' , dpi=300)
# plt.show()
