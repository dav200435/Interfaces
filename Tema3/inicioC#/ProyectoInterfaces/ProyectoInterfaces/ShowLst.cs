using System;
using System.IO;
using System.Windows.Forms;

namespace ProyectoInterfaces
{
    public partial class ShowLst : Form
    {
        private string filePath;

        public ShowLst(string path)
        {
            InitializeComponent();
            this.filePath = path;

            // Asegúrate de que el formulario no sea de nivel superior
            this.TopLevel = false;
            this.FormBorderStyle = FormBorderStyle.None; // Sin bordes
            this.Dock = DockStyle.Fill; // Ocupará todo el contenedor
            ShowInventory();
        }

        private void ShowInventory()
        {
            if (File.Exists(filePath))
            {
                var items = File.ReadAllLines(filePath);
                lstInventory.Items.Clear();
                foreach (var item in items)
                {
                    lstInventory.Items.Add(item);
                }
            }
            else
            {
                MessageBox.Show("El inventario está vacío.", "Aviso", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void ShowLst_Load(object sender, EventArgs e)
        {

        }
    }
}
