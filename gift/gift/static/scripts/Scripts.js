const link = document.querySelector('.link-detail')
const alertAdd = document.querySelector('.alert')
const items = document.querySelectorAll('.cart-add')
const cartItems = document.querySelectorAll('.item-cart')
const sumPrice = document.querySelector('.sum-price')
const del = document.querySelectorAll('.del')
let price = 0
let flag = true

if (link) link.addEventListener('click', e => e.preventDefault())

for (let i = 0; i < items.length; i++) {
  items[i].addEventListener('click', function() {
    localStorage.setItem(this.dataset.id, 'OK')
    alertAdd.style.transform = 'translateY(0)'
    alertAdd.style.opacity = '1'
    setTimeout(function() {
      alertAdd.style.transform = 'translateY(-10vw)'
      alertAdd.style.opacity = '0'
    }, 3000)
  })
}

function updateItems() {
  for (let i = 0; i < cartItems.length; i++) {
    if (!localStorage.getItem(cartItems[i].dataset.id)) {
      cartItems[i].style.display = 'none'
    } else {
      cartItems[i].style.display = 'flex'
      if (flag) {
        price += +cartItems[i].dataset.price
      }
    }
  }
  flag = false
}

updateItems()

sumPrice.textContent = price

for (let i = 0; i < del.length; i++) {
  del[i].addEventListener('click', function() {
    localStorage.removeItem(this.dataset.id)
    updateItems()
    price -= +this.dataset.price
    sumPrice.textContent = price
  })
}
