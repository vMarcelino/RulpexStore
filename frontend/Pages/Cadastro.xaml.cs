using System;
using System.Collections.Generic;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace ProjetoRulpex
{
    /// <summary>
    /// Interação lógica para Cadastro.xam
    /// </summary>
    public partial class Cadastro : Page
    {
        public Cadastro()
        {
            InitializeComponent();
        }

        private void Cadastrar(object sender, RoutedEventArgs e)
        {

        }

        private void Sair(object sender, RoutedEventArgs e)
        {
            this.NavigationService.Navigate(false);
        }

        private void Cancelar(object sender, RoutedEventArgs e)
        {

        }
    }
}
