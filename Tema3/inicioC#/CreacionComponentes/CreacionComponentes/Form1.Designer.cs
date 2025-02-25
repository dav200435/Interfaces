namespace CreacionComponentes
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.miControl1 = new MiControl();
            this.toggleButton1 = new ToggleButton();
            this.SuspendLayout();
            // 
            // miControl1
            // 
            this.miControl1.Location = new System.Drawing.Point(239, 109);
            this.miControl1.Name = "miControl1";
            this.miControl1.Size = new System.Drawing.Size(101, 45);
            this.miControl1.TabIndex = 0;
            this.miControl1.Text = "miControl1";
            this.miControl1.UseVisualStyleBackColor = true;
            // 
            // toggleButton1
            // 
            this.toggleButton1.AutoSize = true;
            this.toggleButton1.Location = new System.Drawing.Point(495, 153);
            this.toggleButton1.MinimumSize = new System.Drawing.Size(45, 22);
            this.toggleButton1.Name = "toggleButton1";
            this.toggleButton1.OffBackColor = System.Drawing.Color.Gray;
            this.toggleButton1.OffToggleColor = System.Drawing.Color.WhiteSmoke;
            this.toggleButton1.OnBackColor = System.Drawing.Color.MediumSlateBlue;
            this.toggleButton1.OnToggleColor = System.Drawing.Color.White;
            this.toggleButton1.Size = new System.Drawing.Size(111, 22);
            this.toggleButton1.SolidStyle = true;
            this.toggleButton1.TabIndex = 1;
            this.toggleButton1.Text = "toggleButton1";
            this.toggleButton1.UseVisualStyleBackColor = true;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.toggleButton1);
            this.Controls.Add(this.miControl1);
            this.Name = "Form1";
            this.Text = "                           ";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private MiControl miControl1;
        private ToggleButton toggleButton1;
    }
}

