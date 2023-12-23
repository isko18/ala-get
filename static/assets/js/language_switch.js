    document.addEventListener('DOMContentLoaded', function () {
        // Находим все элементы с классом language-switch
        const languageSwitches = document.querySelectorAll('.language-switch');

        // Перебираем найденные элементы и назначаем обработчик событий
        languageSwitches.forEach(function (languageSwitch) {
            languageSwitch.addEventListener('click', function () {
                // Получаем язык из атрибута data-language
                const selectedLanguage = languageSwitch.getAttribute('data-language');
                
                // Получаем текущий язык из URL
                const currentLanguage = window.location.pathname.split('/')[1];

                // Инвертируем язык (если текущий ru, то новый ky, и наоборот)
                const newLanguage = (currentLanguage === 'ru') ? 'ky' : 'ru';

                // Формируем новую ссылку с выбранным языком
                const newUrl = window.location.href.replace('/' + currentLanguage + '/', '/' + newLanguage + '/');

                // Переходим по новой ссылке
                window.location.href = newUrl;
            });
        });
    });
