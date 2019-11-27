using System.Diagnostics;
using System.Windows;

namespace ProjetoRulpex
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
            DataContext = MainWindowViewModel.Instance;
            MainWindowViewModel.StartPage(new LoginViewModel());

        }
    }
    public class MainWindowViewModel : BaseViewModel
    {
        public BaseViewModel ApplicationPage { get; set; }
        public string Token;
        private MainWindowViewModel() {/* no instantiation */ }
        public static readonly MainWindowViewModel Instance = new MainWindowViewModel();
        public static void StartPage(BaseViewModel page)
        {
            Trace.WriteLine("Page changing");
            Instance.ApplicationPage = page;
            Trace.WriteLine("Page changed");
            page.Initialize();
            Trace.WriteLine("Page initialized");
            //(nameof(ApplicationPage));
        }
    }
}
