button = document.getElementById('archivebtn')
archive_block = document.getElementById('archive_block')
button.addEventListener('click', () => {
  archive_block.style.display = 'flex';
});

const punish_buttons = document.querySelectorAll('#punishbtn');

punish_buttons.forEach((punish) => {
  punish.addEventListener('click', (event) => {
    const common_ancestor = event.currentTarget.closest('.inner_report_block');
    const punish_block = common_ancestor.querySelector('#punish_block');
    punish_block.style.display = 'flex';
  });
});