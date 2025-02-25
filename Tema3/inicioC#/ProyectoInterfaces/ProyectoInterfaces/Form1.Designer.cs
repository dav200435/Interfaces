namespace ProyectoInterfaces
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.menuPanel = new System.Windows.Forms.Panel();
            this.exitBtn = new System.Windows.Forms.Button();
            this.Refresh = new System.Windows.Forms.Button();
            this.showLstBtn = new System.Windows.Forms.Button();
            this.removeElementBtn = new System.Windows.Forms.Button();
            this.addElementBtn = new System.Windows.Forms.Button();
            this.container = new System.Windows.Forms.Panel();
            this.menuPanel.SuspendLayout();
            this.SuspendLayout();
            // 
            // menuPanel
            // 
            this.menuPanel.BackColor = System.Drawing.SystemColors.MenuBar;
            this.menuPanel.Controls.Add(this.exitBtn);
            this.menuPanel.Controls.Add(this.Refresh);
            this.menuPanel.Controls.Add(this.showLstBtn);
            this.menuPanel.Controls.Add(this.removeElementBtn);
            this.menuPanel.Controls.Add(this.addElementBtn);
            this.menuPanel.Dock = System.Windows.Forms.DockStyle.Left;
            this.menuPanel.Location = new System.Drawing.Point(0, 0);
            this.menuPanel.Name = "menuPanel";
            this.menuPanel.Size = new System.Drawing.Size(200, 450);
            this.menuPanel.TabIndex = 0;
            // 
            // exitBtn
            // 
            this.exitBtn.Location = new System.Drawing.Point(54, 387);
            this.exitBtn.Name = "exitBtn";
            this.exitBtn.Size = new System.Drawing.Size(75, 23);
            this.exitBtn.TabIndex = 4;
            this.exitBtn.Text = "Salir";
            this.exitBtn.UseVisualStyleBackColor = true;
            this.exitBtn.Click += new System.EventHandler(this.exitBtn_Click);
            // 
            // Refresh
            // 
            this.Refresh.BackgroundImage = ((System.Drawing.Image)(resources.GetObject("Refresh.BackgroundImage")));
            this.Refresh.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.Refresh.Location = new System.Drawing.Point(123, 22);
            this.Refresh.Name = "Refresh";
            this.Refresh.Size = new System.Drawing.Size(51, 43);
            this.Refresh.TabIndex = 3;
            this.Refresh.UseVisualStyleBackColor = true;
            this.Refresh.Click += new System.EventHandler(this.Refresh_Click);
            // 
            // showLstBtn
            // 
            this.showLstBtn.Location = new System.Drawing.Point(12, 238);
            this.showLstBtn.Name = "showLstBtn";
            this.showLstBtn.Size = new System.Drawing.Size(173, 30);
            this.showLstBtn.TabIndex = 2;
            this.showLstBtn.Text = "Mostrar Lista";
            this.showLstBtn.UseVisualStyleBackColor = true;
            this.showLstBtn.Click += new System.EventHandler(this.showLstBtn_Click);
            // 
            // removeElementBtn
            // 
            this.removeElementBtn.Location = new System.Drawing.Point(12, 182);
            this.removeElementBtn.Name = "removeElementBtn";
            this.removeElementBtn.Size = new System.Drawing.Size(173, 35);
            this.removeElementBtn.TabIndex = 1;
            this.removeElementBtn.Text = "Eliminar Elemento";
            this.removeElementBtn.UseVisualStyleBackColor = true;
            this.removeElementBtn.Click += new System.EventHandler(this.removeElementBtn_Click);
            // 
            // addElementBtn
            // 
            this.addElementBtn.Location = new System.Drawing.Point(11, 128);
            this.addElementBtn.Name = "addElementBtn";
            this.addElementBtn.Size = new System.Drawing.Size(173, 30);
            this.addElementBtn.TabIndex = 0;
            this.addElementBtn.Text = "Agregar Elemento";
            this.addElementBtn.UseVisualStyleBackColor = true;
            this.addElementBtn.Click += new System.EventHandler(this.addElementBtn_Click);
            // 
            // container
            // 
            this.container.AutoScroll = true;
            this.container.Dock = System.Windows.Forms.DockStyle.Fill;
            this.container.Location = new System.Drawing.Point(200, 0);
            this.container.Name = "container";
            this.container.Size = new System.Drawing.Size(600, 450);
            this.container.TabIndex = 1;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.container);
            this.Controls.Add(this.menuPanel);
            this.Name = "Form1";
            this.Text = "Form1";
            this.menuPanel.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel menuPanel;
        private System.Windows.Forms.Button exitBtn;
        private System.Windows.Forms.Button Refresh;
        private System.Windows.Forms.Button removeElementBtn;
        private System.Windows.Forms.Button addElementBtn;
        private System.Windows.Forms.Button showLstBtn;
        private System.Windows.Forms.Panel container;
    }
}

