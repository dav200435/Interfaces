using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows.Forms;

namespace ProyectoInterfaces
{
    public partial class removeItemShow : Form
    {
        private string filePath;

        public removeItemShow(string path)
        {
            InitializeComponent();
            this.filePath = path;

            // Asegúrate de que el formulario no sea de nivel superior
            this.TopLevel = false;
            this.FormBorderStyle = FormBorderStyle.None; // Sin bordes
            this.Dock = DockStyle.Fill; // Ocupará todo el contenedor
            this.filePath = filePath;
            LoadItems();
        }

        private void LoadItems()
        {
            if (File.Exists(filePath))
            {
                var items = File.ReadAllLines(filePath);
                lstItems.DataSource = items.ToList();
            }
            else
            {
                MessageBox.Show("No hay elementos en el inventario.", "Aviso", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void removeButton_Click(object sender, EventArgs e)
        {
            string selectedItem = (string)lstItems.SelectedItem;

            if (!string.IsNullOrEmpty(selectedItem))
            {
                var items = File.ReadAllLines(filePath).ToList();
                items.Remove(selectedItem);

                File.WriteAllLines(filePath, items);
                MessageBox.Show("Elemento eliminado.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
                LoadItems(); // Recargar la lista
            }
            else
            {
                MessageBox.Show("Seleccione un elemento para eliminar.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
