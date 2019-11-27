using Flurl.Http;
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Controls;
using System.Windows.Input;

namespace ProjetoRulpex
{

    class LoginViewModel : BaseViewModel
    {
        public string Username { get; set; }
        public ICommand LoginCommand { get; set; }
        public LoginViewModel()
        {
            LoginCommand = new RelayParametrizedCommand(LoginRequested);
        }
        private async void LoginRequested(object passwordObject)
        {
            string password = (passwordObject as PasswordBox).Password;
            if (await CredenciaisValidas(Username, password))
            {
                //MainWindowViewModel.ApplicationPage = new
                Trace.WriteLine("deu bom");
                MainWindowViewModel.StartPage(new CatalogoViewModel());
                Trace.WriteLine("pronto");
            }
            else
            {
                Trace.WriteLine("Deu bom n");
            }
        }

        private async Task<bool> CredenciaisValidas(string user, string password)
        {
            try
            {
                var result = await "http://127.0.0.1:1234/signin".AllowHttpStatus(HttpStatusCode.Accepted).PostJsonAsync(new { user = user, password = password }).ReceiveJson<TokenHolder>();
                Trace.WriteLine("Result: " + result.token);
                MainWindowViewModel.Instance.Token = result.token;
                return true;
            }
            catch (Exception e)
            {
                Trace.WriteLine(e.Message);
            }
            return false;
        }
        private class TokenHolder
        {
            public string token { get; set; }
        }
    }
}
