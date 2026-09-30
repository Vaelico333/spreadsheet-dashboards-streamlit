# Inventory management dashboard

A dashboard that explores how a pharmacy store manages its inventory and relationship with its providers.
The dataset is forged and completely artificial, but coherent.

---

Inventory management is a crucial part of any business. Before we had computers, it was a difficult job, where you had to be aware of all the stock you had in your warehouse, review it on a daily or weekly basis, and calculate KPIs using pen and paper. By using Excel worksheets and data analysis, we can register all stock and money movements, automatically calculate KPIs and extract some valuable and actionable insight that will surely be very useful to any business.

### Purpose of this project

This project aims to transform raw data into a clear, visually engaging dashboard that reveals underlying structures and relationships between features. By leveraging Excel’s dynamic tables and interactive slicers, the design allows users to explore these relationships in detail, with key findings highlighted through targeted plots, tables and KPIs.

### The dataset

The dataset explored in this project, created by an anonymous person, contains 950 entries with 15 features:

- **Fecha_Pedido**: it's the date when the current order was emitted. It goes from the 1st of January 2022 to the 14th of December 2022.
- **Mes_Texto**: it's the month of the current entry, written in text.
- **Trimestre**: it's the quarter of the year of the current entry.
- **#_Semana**: it's the week number of the current entry. It goes from 1 to 51.
- **Código_Producto**: it's the product codenumber. It goes from *CP00001* to *CP00020*.
- **Producto**: it's the product's name. There are 20 different products.
- **Cantidad**: it's the quantity of product bought in this entry.
- **Precio U.**: it's the unit price of the product in bought in this entry.
- **Precio Total**: it's the total price of the products bought in this entry. It's calculated by multiplying *Cantidad* by *Precio U.*
- **Estado_Pedido**: it's the product's delivery status. It can be *Recibido* (received), *Pendiente* (pending) or *Devuelto* (returned to sender).
- **Código_Proveedor**: it's the provider's internal code. It ranges from *P0001* to *P0005*.
- **Proveedor**: it's the provider's company name.
- **Fecha_Entrega**: it's the date in which the order was delivered. If it's still pending, the date is 00/01/1900.
- **Tiempo_Entrega(Días)**: it's the time it took for the provider to deliver the product, in days.
Another table was provided, containing **sales** data, in the form of euros per month.

### Workflow

This dashboard was built the following way:  
  
Excel table  
**↓**  
Create dynamic tables  
**↓**  
Create plots and tables  
**↓**  
Add data slicers  
**↓**  
Setup and format the dashboard  

---

The dashboard is structured as follows:

### KPIs

I chose to display seven KPIs:

- **Total amount of products** and total price: it's the amount of products, and their total price, included in the current view of the dashboard.
- **Received products** and their price: it's the amount of products, and their price, that were successfully delivered by the providers.
- **Returned products** and their price: it's the amount of products, and their price, that were returned to the provider for unspecified causes.
- **Pending products** and their price: it's the amount of products, and their price, that have been ordered, but not delivered yet.
- **% of products bought vs products sold**: it's the proportion between the costs of products bought and the money earned by sales.
- **Average number of products ordered**: it's the mean average of products ordered per order.
- **Average delivery time (in days)**: it's the mean average of the time it took for the provider or providers to deliver the products.

These KPIs give us an idea of the size of the current dataset, the providers' and clients' behaviour and our business needs.

### Tables

In order to show some useful facts, I created two tables to show these rankings:

- **Best selling products**: it shows the five best selling products, and their mean average quantity sold, their total quantity sold and the total money earned by selling them.
- **Worst selling products**: it shows the five worst selling products, and their mean average quantity sold, their total quantity sold and the total money earned by selling them.  

As this was one of my first projects, I used screenshots of the tables to show on the dashboard. In the future, I would like to find a better way to show these tables, so that it can be dinamically modified using the filters and data slicers.

### Plots

Using several types of charts, I explored relationships between features in the dataset:

- <u>**Lineplot**</u>:
    - **Amount of products ordered by month**: this plot shows the amount of products that were ordered on a monthly basis.
    - **Amount of products ordered by week**: this plot shows the amount of products that were ordered on a weekly basis.
- <u>**Horizontal barplot**</u>:
    - **Amount of products**: this plot shows the total amount of products of each type ordered.  
- <u>**Pieplot**</u>:
    - **Total orders in this period**: this plot shows the total amount of orders in the current period, and three pie plots, showing the proportion of received, returned and pending orders.

### Slicers

To segment and navigate the data more easily, I included the following slicers, which allow users to view different parts of the dataset in the plots:

- **Order status**: received, pending and returned.
- **Month**: January to December.
- **Quarter**: T1 to T4.
- **Semester**: Sem1 and Sem2.
- **Provider**: Comercial Mili, Corpora Xauxa S.R.L., Distribuidora Ric and Super Ventas.

---

### Observations

- The dataset contains 950 entries, each one corresponding to one product ordered to one provider. The total of products amounts to 12,260, and there are 10,745 products received, 1,087 returned and 428 pending. The only month with pending products is December.
- In average, the amount of products returned is about 10% of the ones received and accepted. March stands out with a 24.7% of returned products.
- The average delivery time ranges from 1.92 (Corpora Xauxa S.R.L.) to 3.89 days (Distribuidora Ric).
- Event though *Paracetamol* is the best selling product, it's not the most profitable: *Antiinflamatorio*, *Gel* and *Antibióticos* are more expensive, and selling them is more profitable.

### Case study: Choosing providers

Sometimes, a business needs to let go of a provider, if it's not performing as expected. In this case study, I will review all the data from this dashboard in order to select the worst provider, and decide if it's bad enough to end our relationship with them.

**Observations**:  


**Observations**:  


**Observations**:  


**Observations**:  

#### Conclussions and recommendations


My **recommendations**:


---

### Challenges

The main challenge in this project was organizing the data and choosing the right plots to provide actionable insights from the raw data. Once that was done, creating the dynamic tables and adding slicers was relatively straightforward.

Excel is a powerful tool, although it can be somewhat cumbersome because of its high memory consumption and susceptibility to errors.

### Skills trained

Through this project, I improved my spreadsheet skills by learning how to create, manage and filter dynamic tables and charts, and how to combine them into a clear, engaging and visually appealing dashboard.