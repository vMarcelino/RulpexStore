using System;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using Flurl.Http;

namespace ProjetoRulpex
{
    /// <summary>
    /// Interação lógica para Login.xam
    /// </summary>
    public partial class Login : Page
    {
        public Login()
        {
            InitializeComponent();
        }


        private void Sair(object sender, RoutedEventArgs e)
        {
            Application.Current.Shutdown();
        }
    }
}
