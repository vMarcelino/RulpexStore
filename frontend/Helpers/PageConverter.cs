using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Globalization;
using System.Text;
using System.Windows.Data;

namespace ProjetoRulpex
{
    public class PageConverter : BaseValueConverter<PageConverter>
    {
        public override object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            switch ((BaseViewModel)value)
            {
                case LoginViewModel vm:
                    return new Login() { DataContext = vm };

                case CatalogoViewModel vm:
                    return new Catalogo() { DataContext = vm };

                case ItemDisplayViewModel vm:
                    return new ItemDisplay() { DataContext = vm };

                case CadastroViewModel vm:
                    return new Cadastro() { DataContext = vm };

                default:
                    Debugger.Break();
                    throw new NotImplementedException();
            }
        }

        public override object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
