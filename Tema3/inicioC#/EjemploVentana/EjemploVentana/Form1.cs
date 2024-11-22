using System;
using System.Collections.Generic;
using System.Windows.Forms;

namespace EjemploVentana
{
    public partial class Form1 : Form
    {
        List<Cita> citas = new List<Cita>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Configurar ListView para mostrar columnas
            lvCitas.View = View.Details;
            lvCitas.Columns.Add("Nombre", 150);
            lvCitas.Columns.Add("Fecha", 100);
            lvCitas.Columns.Add("Hora", 100);
        }

        private void btnReservar_Click(object sender, EventArgs e)
        {
            var nuevaCita = new Cita
            {
                Nombre = txtNombre.Text,
                Fecha = datePicker.Value,
                Hora = datePicker.Value.ToShortTimeString()
            };
            citas.Add(nuevaCita);
            MessageBox.Show("Cita reservada.");
            ActualizarListaCitas();
        }

        private void ActualizarListaCitas()
        {
            lvCitas.Items.Clear(); // Limpiar la lista

            foreach (var cita in citas)
            {
                var item = new ListViewItem(cita.Nombre); // Primer columna
                item.SubItems.Add(cita.Fecha.ToShortDateString()); // Segunda columna
                item.SubItems.Add(cita.Hora); // Tercera columna
                lvCitas.Items.Add(item);
            }
        }

        private void btnVerCitas_Click(object sender, EventArgs e)
        {
            ActualizarListaCitas(); // También usa el método para actualizar
        }
    }
}
