using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Formulario
{
    public partial class Form1 : Form
    {

        public Form1()
        {
            InitializeComponent();

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void txtNombre_TextChanged(object sender, EventArgs e)
        {

        }

        private void Correo_TextChanged(object sender, EventArgs e)
        {

        }

        private void txtTelefono_TextChanged(object sender, EventArgs e)
        {
            Console.log("editado");
        }

        private void btnSalir_Click_1(object sender, EventArgs e)
        {
            // Cerrar la aplicación
            Application.Exit();
        }

        private void btnVerDatos_Click(object sender, EventArgs e)
        {
            Form3 form2 = new Form3();
            form2.Show(); // Muestra el segundo formulario
        }

        private void btnGuardar_Click(object sender, EventArgs e)
        {
            // Datos a guardar
            string nombre = txtNombre.Text;
            string correo = txtCorreo.Text;
            int telefono = int.Parse(txtTelefono.Text);
            int edad = int.Parse(txtEdad.Text);

            // Validar que no estén vacíos
            if (string.IsNullOrWhiteSpace(nombre) || string.IsNullOrWhiteSpace(correo) || !int.TryParse(txtTelefono.Text, out telefono) || !int.TryParse(txtEdad.Text, out edad))
            {
                MessageBox.Show("Por favor, completa todos los campos antes de guardar.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            // Ruta del archivo CSV
            string rutaArchivo = "datos.csv";

            try
            {
                // Verificar si el archivo existe para escribir el encabezado solo la primera vez
                bool archivoExiste = File.Exists(rutaArchivo);

                using (StreamWriter writer = new StreamWriter(rutaArchivo, true))
                {
                    // Escribir encabezado si es la primera vez
                    if (!archivoExiste)
                    {
                        writer.WriteLine("Nombre,Correo,Teléfono,Edad");
                    }

                    // Escribir datos
                    writer.WriteLine($"{nombre},{correo},{telefono},{edad}");
                }

                // Confirmación
                MessageBox.Show("Datos guardados correctamente.", "Éxito", MessageBoxButtons.OK, MessageBoxIcon.Information);

                // Limpiar los campos del formulario
                txtNombre.Clear();
                txtCorreo.Clear();
                txtTelefono.Clear();
                txtEdad.Clear();
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Ocurrió un error al guardar los datos: {ex.Message}", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void txtEdad_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
