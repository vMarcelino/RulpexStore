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

    class CatalogoViewModel : BaseViewModel
    {
        public ObservableCollection<ItemDisplayViewModel> items { get; set; }
        public ICommand AddItemCommand { get; set; }

        public CatalogoViewModel()
        {
            AddItemCommand = new RelayCommand(AddItem);
        }
        private void AddItem()
        {
            MainWindowViewModel.StartPage(new CadastroViewModel());
        }

        public override async void Initialize()
        {
            items = new ObservableCollection<ItemDisplayViewModel>();
            var results = await "http://127.0.0.1:1234/item".GetJsonAsync<Dictionary<string, List<camisetaInfo>>>();
            foreach (var result in results)
            {
                Trace.WriteLine(result.Key);
                foreach (var value in result.Value)
                {
                    ItemDisplayViewModel newItem = new ItemDisplayViewModel()
                    {
                        cat = "Em: " + result.Key,
                        Descr = value.description,
                        Nome = value.name,
                        Valor = "R$" + value.value.ToString()
                    };
                    items.Add(newItem);
                }
                Trace.WriteLine("");
            }
        }
        private class camisetaInfo
        {
            public string name { get; set; }
            public float value { get; set; }
            public string description { get; set; }
            public string image { get; set; }
            public int id { get; set; }
        }
    }
}
