using Flurl.Http;
using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Diagnostics;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows.Input;

namespace ProjetoRulpex
{

    class CadastroViewModel : BaseViewModel
    {
        public ICommand CadastrarCommand { get; set; }
        public ICommand CancelarCommand { get; set; }
        public string Name { get; set; }
        public string Descr { get; set; }
        public string Cat { get; set; }
        public string Value { get; set; }
        public CadastroViewModel()
        {
            CadastrarCommand = new RelayCommand(cadastrar);
            CancelarCommand = new RelayCommand(voltar);
        }
        private async void cadastrar()
        {
            try
            {
                var result = await "http://127.0.0.1:1234/item".AllowHttpStatus(HttpStatusCode.Accepted).PostJsonAsync(new
                {
                    token = MainWindowViewModel.Instance.Token,
                    name = Name,
                    description = Descr,
                    value = Value,
                    catalog = Cat
                }).ReceiveString();
                Trace.WriteLine("result: " + result);
                voltar();
            }
            catch (Exception e)
            {
                Trace.WriteLine(e.Message);
            }
        }
        private void voltar()
        {
            MainWindowViewModel.StartPage(new CatalogoViewModel());
        }
    }
}
