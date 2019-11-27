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

    class ItemDisplayViewModel : BaseViewModel
    {
        public string Nome { get; set; }
        public string Valor { get; set; }
        public string Descr { get; set; }
        public string cat { get; set; }
    }
}
