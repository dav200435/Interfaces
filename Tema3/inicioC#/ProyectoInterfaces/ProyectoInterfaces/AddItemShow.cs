using System;
using System.IO;
using System.Windows.Forms;

namespace ProyectoInterfaces
{
    public partial class AddItemShow : Form
    {
        private string filePath;

        public AddItemShow(string path)
        {
            InitializeComponent();
            this.filePath = path;

            // Asegúrate de que el formulario no sea de nivel superior
            this.TopLevel = false;
            this.FormBorderStyle = FormBorderStyle.None; // Sin bordes
            this.Dock = DockStyle.Fill; // Ocupará todo el contenedor
        }

        private void AddBtn_Click(object sender, EventArgs e)
        {
            string newItem = txtItemName.Text.Trim();
            if (!string.IsNullOrEmpty(newItem))
            {
                // Agregar el elemento al archivo
                File.AppendAllText(filePath, newItem + Environment.NewLine);
                MessageBox.Show("Elemento agregado exitosamente.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);
                txtItemName.Clear();
            }
            else
            {
                MessageBox.Show("Por favor, ingrese un nombre válido.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
