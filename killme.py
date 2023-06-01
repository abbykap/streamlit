import streamlit as st
import pandas as pd
import os
import dask.dataframe as dd
import matplotlib.pyplot as plt
import numpy as np
import mpld3
import streamlit.components.v1 as components
import io
from streamlit_extras.let_it_rain import rain



st.title('Darshan Log Graph Generator!')

uploaded_files = st.file_uploader("Upload those Darshan Logs son!", type="csv", accept_multiple_files=True)
if uploaded_files:
    for file in uploaded_files:
        file.seek(0)
    uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    df = pd.concat(uploaded_data_read)

    rain(
        emoji="🌸",
        font_size=54,
        falling_speed=4,
        animation_length=.2,
    )

    with st.container():
        col1, col2 = st.columns(2)
    with col1:
        st.subheader('This is a subheader')
    with col2:
        tab1, tab2= st.tabs(["Write", "Read"])
        with tab1:
            lustre_columns2 = ['POSIX_SIZE_WRITE_0_100', 'POSIX_SIZE_WRITE_100_1K', 'POSIX_SIZE_WRITE_1K_10K', 'POSIX_SIZE_WRITE_10K_100K', 'POSIX_SIZE_WRITE_100K_1M', 'POSIX_SIZE_WRITE_1M_4M', 'POSIX_SIZE_WRITE_4M_10M', 'POSIX_SIZE_WRITE_10M_100M', 'POSIX_SIZE_WRITE_100M_1G', 'POSIX_SIZE_WRITE_1G_PLUS']
            lustre_counts2 = df[lustre_columns2].nunique()
            total_lustre_cells2 = lustre_counts2.sum()
            ecdf2 = np.concatenate(([0], np.cumsum(lustre_counts2) / total_lustre_cells2))
            fig, ax = plt.subplots()
            ax.plot(ecdf2, label='CDF', color='pink')
            ax.legend()
            ax.set_xlabel('Percentage of Calls')
            ax.set_ylabel('Percentage of Files')
            ax.set_xticks(np.linspace(0, len(lustre_columns2) + 1,len(lustre_columns2) + 1))
            ax.set_xticklabels(['0'] + lustre_columns2, rotation=45, ha='right')
            ax.set_xlim(left=0)
            ax.set_ylim(0, 1)
            ax.set_yticks(np.linspace(0, 1, 11))
            ax.set_yticklabels(['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])
            st.pyplot(fig)
        with tab2:
            lustre_columns = ['POSIX_SIZE_READ_0_100', 'POSIX_SIZE_READ_100_1K', 'POSIX_SIZE_READ_1K_10K', 'POSIX_SIZE_READ_10K_100K', 'POSIX_SIZE_READ_100K_1M', 'POSIX_SIZE_READ_1M_4M', 'POSIX_SIZE_READ_4M_10M', 'POSIX_SIZE_READ_10M_100M', 'POSIX_SIZE_READ_100M_1G', 'POSIX_SIZE_READ_1G_PLUS']
            lustre_counts = df[lustre_columns].nunique()
            total_lustre_cells = lustre_counts.sum()
            ecdf = np.concatenate(([0], np.cumsum(lustre_counts) / total_lustre_cells))
            fig, ax = plt.subplots()
            ax.plot(ecdf, label='CDF', color='pink')
            ax.legend()
            ax.set_xlabel('Percentage of Calls')
            ax.set_ylabel('Percentage of Files')
            ax.set_xticks(np.linspace(0, len(lustre_columns) + 1,len(lustre_columns) + 1))
            ax.set_xticklabels(['0'] + lustre_columns, rotation=45, ha='right')
            ax.set_xlim(left=0)
            ax.set_ylim(0, 1)
            ax.set_yticks(np.linspace(0, 1, 11))
            ax.set_yticklabels(['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'])
            st.pyplot(fig)

    with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.subheader('This is a subheader')
            with col2:
                tab1, tab2= st.tabs(["Write", "Read"])
                with tab1:
                    lustre_columns3 = ['POSIX_CONSEC_READS', 'POSIX_SEQ_READS']
                    lustre_counts3 = df[lustre_columns3].nunique()
                    total_lustre_cells3 = lustre_counts3.sum()
                    lustre_columns4 = ['POSIX_CONSEC_WRITES', 'POSIX_SEQ_WRITES']
                    lustre_counts5 = df[lustre_columns4].nunique()
                    total_lustre_cells6 = lustre_counts5.sum()
                    shit = ['POSIX_CONSEC_READS']
                    shit2 = df[shit].nunique()
                    shit3 = shit2.sum()
                    shit4 = ['POSIX_SEQ_READS']
                    shit5 = df[shit4].nunique()
                    shit6 = shit5.sum()
                    shit7 = ['POSIX_CONSEC_WRITES']
                    shit8 = df[shit7].nunique()
                    shit9 = shit8.sum()
                    shit11 = ['POSIX_SEQ_WRITES']
                    shit12 = df[shit11].nunique()
                    shit13 = shit12.sum()
                    consec_read_pct = shit3 / total_lustre_cells3 * 100
                    consec_read_pct2 = shit6 / total_lustre_cells3 * 100
                    consec_read_pct3 = shit9 / total_lustre_cells6 * 100
                    consec_read_pct4 = shit13 / total_lustre_cells6 * 100
                    # create bar chart
                    fig, ax = plt.subplots()
                    x = ['Consecutive Writes', 'Sequential Writes']
                    y = [consec_read_pct, consec_read_pct2]
                    pink_color = (1.0, 0.6, 0.6)  # RGB values for pink
                    ax.bar(x, y, color=pink_color)
                    ax.set_ylabel('Percentage')
                    ax.set_ylim(0, 100)
                    st.pyplot(fig)

                with tab2:
                    fig, ax = plt.subplots()
                    x = ['Consecutive Reads', 'Sequential Reads']
                    y = [consec_read_pct3, consec_read_pct4]
                    ax.bar(x, y, color=pink_color)
                    ax.set_ylabel('Percentage')
                    ax.set_ylim(0, 100)
                    st.pyplot(fig)


            
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader('This is a subheader')
        with col2:
            io_columns = ['POSIX_CONSEC_READS', 'POSIX_CONSEC_WRITES', 'POSIX_SEQ_READS', 'POSIX_SEQ_WRITES']
            io_count = df[io_columns].count().sum()
            metadata_columns = ['POSIX_OPENS', 'POSIX_SEEKS', 'POSIX_STATS']
            metadata_count = df[metadata_columns].count().sum()
            io_pct = io_count / (io_count + metadata_count) * 100
            metadata_pct = metadata_count / (io_count + metadata_count) * 100
            fig, ax = plt.subplots()
            x = ['I/O operations', 'Metadata operations']
            y = [io_pct, metadata_pct]
            ax.bar(x, y, color=pink_color)
            ax.set_ylabel('Percentage')
            ax.set_ylim(0, 100)
            st.pyplot(fig)    
        
else:
    st.write("No files uploaded.")

