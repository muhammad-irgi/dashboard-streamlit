import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# membaca dataset
main_dataset = pd.read_csv('main_dataset.csv')

st.title("Dashboard Penyewaan Sepeda")

st.header("Total Penyewaan Sepeda")
total_rentals = main_dataset['cnt_x'].sum()
st.metric(label="Total Penyewaan Sepeda", value=total_rentals)

st.title('Belajar Analisis Data')
by_day, by_hour = st.tabs(["By Day", "By Hour"])

with by_day:
    st.header("By Day")
    season_counts = main_dataset.groupby('season_x')['cnt_x'].sum()
    season_labels = {
        1: 'Musim Dingin',
        2: 'Musim Semi',
        3: 'Musim Panas',
        4: 'Musim Gugur'
    }
    season_counts.index = season_counts.index.map(season_labels)
    fig, ax = plt.subplots()
    ax.pie(season_counts, labels=season_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.header("Total Penyewaan Sepeda Berdasarkan Musim")
    st.pyplot(fig)

    main_dataset['dteday_x'] = pd.to_datetime(main_dataset['dteday_x'], format='%Y-%m-%d')

    # membuat data set 2011 dan 2012
    data_2011 = main_dataset[main_dataset['dteday_x'].dt.year == 2011]
    data_2012 = main_dataset[main_dataset['dteday_x'].dt.year == 2012]

    # grouping data
    month_counts_2011 = data_2011.groupby('mnth_x')['cnt_x'].sum()
    month_counts_2012 = data_2012.groupby('mnth_x')['cnt_x'].sum()

    # label nama nama bulan
    month_labels = {
        1: 'Januari',
        2: 'Februari',
        3: 'Maret',
        4: 'April',
        5: 'Mei',
        6: 'Juni',
        7: 'Juli',
        8: 'Agustus',
        9: 'September',
        10: 'Oktober',
        11: 'November',
        12: 'Desember'
    }

    # memilah data untuk dibedakan 2011 dan 2012
    month_counts_2011.index = month_counts_2011.index.map(month_labels)
    month_counts_2012.index = month_counts_2012.index.map(month_labels)

    by_2011, by_2012 = st.tabs(["2011", "2012"])
    with by_2011:    
        # membuat plot line chart untuk 2011
        fig1, ax1 = plt.subplots()
        ax1.plot(month_counts_2011.index, month_counts_2011.values, marker='o', linestyle='-', color='b')
        ax1.set_xlabel('Month')
        ax1.set_ylabel('Total Rentals')
        ax1.set_title('Total Rentals per Month (2011)')
        plt.xticks(rotation=45)  
        st.header("Total Rentals per Month (2011)")
        st.pyplot(fig1)

    with by_2012:
        # membuat plot line chart untuk 2012
        fig2, ax2 = plt.subplots()
        ax2.plot(month_counts_2012.index, month_counts_2012.values, marker='o', linestyle='-', color='r')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Total Rentals')
        ax2.set_title('Total Rentals per Month (2012)')
        plt.xticks(rotation=45)  
        st.header("Total Rentals per Month (2012)")
        st.pyplot(fig2)


with by_hour:
    st.header("By Hour")
    st.header("Jumlah Penyewaan Sepeda Berdasarkan Jam")
    hour_counts = main_dataset.groupby('hr')['cnt_y'].sum()

    fig, ax = plt.subplots(figsize=(10, 5))  # Create a figure and axis
    ax.bar(hour_counts.index, hour_counts.values, color='orange')
    ax.set_title('Jumlah Penyewaan Sepeda Berdasarkan Jam')
    ax.set_xlabel('Jam dalam Sehari')
    ax.set_ylabel('Jumlah Penyewaan Sepeda (cnt_y)')
    st.pyplot(fig)  # Pass the figure to st.pyplot()
