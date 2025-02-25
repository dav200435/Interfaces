using System;
using System.IO;
using System.Windows.Forms;

namespace ProyectoInterfaces
{
    public partial class Form1 : Form
    {
        private string inventoryFile = "inventario.txt"; // Archivo de almacenamiento

        public Form1()
        {
            InitializeComponent();
        }

        // Método para mostrar formularios dentro del panel "container"
        private void LoadFormIntoContainer(Form form)
        {
            // Limpia el panel antes de agregar un nuevo formulario
            container.Controls.Clear();

            // Configuración necesaria para el formulario hijo
            form.TopLevel = false;                      // No es de nivel superior
            form.FormBorderStyle = FormBorderStyle.None; // Sin bordes
            form.Dock = DockStyle.Fill;                 // Ocupa todo el espacio del panel

            // Agregar y mostrar el formulario dentro del panel
            container.Controls.Add(form);               // Agrega el formulario al panel
            container.Tag = form;                       // Asocia el formulario al panel (opcional)
            form.Show();                                // Muestra el formulario
        }

        // Método para refrescar la vista principal (opcional)
        private void Refresh_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Refrescando la vista principal...");
        }

        // Abre la vista para agregar un elemento dentro del panel
        private void addElementBtn_Click(object sender, EventArgs e)
        {
            AddItemShow addItemForm = new AddItemShow("inventario.txt");
            LoadFormIntoContainer(addItemForm);
        }

        // Abre la vista para eliminar un elemento dentro del panel
        private void removeElementBtn_Click(object sender, EventArgs e)
        {
            removeItemShow removeItemForm = new removeItemShow("inventario.txt");
            LoadFormIntoContainer(removeItemForm);
        }

        // Abre la vista para mostrar los elementos dentro del panel
        private void showLstBtn_Click(object sender, EventArgs e)
        {
            ShowLst showLstForm = new ShowLst("inventario.txt");
            LoadFormIntoContainer(showLstForm);
        }

        // Cierra la aplicación
        private void exitBtn_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
