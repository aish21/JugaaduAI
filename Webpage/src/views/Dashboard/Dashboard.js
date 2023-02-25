/*!

=========================================================
* Vision UI Free Chakra - v1.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/vision-ui-free-chakra
* Copyright 2021 Creative Tim (https://www.creative-tim.com/)
* Licensed under MIT (https://github.com/creativetimofficial/vision-ui-free-chakra/blob/master LICENSE.md)

* Design and Coded by Simmmple & Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
// Chakra imports
import {
	Box,
	Button,
	CircularProgress,
	CircularProgressLabel,
	Flex,
	Grid,
	Icon,
	Progress,
	SimpleGrid,
	Spacer,
	Stack,
	Stat,
	StatHelpText,
	StatLabel,
	StatNumber,
	Table,
	Tbody,
	Text,
	Th,
	Thead,
	Tr
} from '@chakra-ui/react';
// Styles for the circular progressbar
import medusa from 'assets/img/WelcomeBack.jpg';
import medusa1 from 'assets/img/EditBg.png';
import medusa2 from 'assets/img/EditBg_2.png';
import trim from 'assets/img/Trim.png';
import combine from 'assets/img/Combine.png';
import autocaptions from 'assets/img/Autocaptions.jpg';
import denoise from 'assets/img/Denoising.jpg';
import colourcorrection from 'assets/img/ColourCorrection.jpg';
import compression from 'assets/img/Compression.jpeg';
import speed from 'assets/img/Speed.jpg';
import bgmusic from 'assets/img/BgMusic.jpg';
// Custom components
import Card from 'components/Card/Card.js';
import CardBody from 'components/Card/CardBody.js';
import CardHeader from 'components/Card/CardHeader.js';
import BarChart from 'components/Charts/BarChart';
import LineChart from 'components/Charts/LineChart';
import IconBox from 'components/Icons/IconBox';
// Icons
import { CartIcon, DocumentIcon, GlobeIcon, RocketIcon, StatsIcon, WalletIcon } from 'components/Icons/Icons.js';
import DashboardTableRow from 'components/Tables/DashboardTableRow';
import TimelineRow from 'components/Tables/TimelineRow';
import React from 'react';
import { AiFillCheckCircle } from 'react-icons/ai';
import { BiHappy } from 'react-icons/bi';
import { BsArrowRight } from 'react-icons/bs';
import { IoCheckmarkDoneCircleSharp, IoEllipsisHorizontal } from 'react-icons/io5';
// Data
import {
	barChartDataDashboard,
	barChartOptionsDashboard,
	lineChartDataDashboard,
	lineChartOptionsDashboard
} from 'variables/charts';
import { dashboardTableData, timelineData } from 'variables/general';

export default function Dashboard() {
	return (
		<Flex flexDirection='column' pt={{ base: '120px', md: '75px' }}>
			
			<Grid templateColumns={{ sm: '1fr', md: '1fr 1fr', '2xl': '2fr 1.2fr 1.5fr' }} my='26px' gap='18px'>
				{/* Welcome Card */}
				<Card
					p='0px'
					gridArea={{ md: '1 / 1 / 2 / 3', '2xl': 'auto' }}
					bgImage={medusa}
					bgSize='cover'
					bgPosition='30%'>
					<CardBody w='100%' h='100%'>
						<Flex flexDirection={{ sm: 'column', lg: 'row' }} w='100%' h='100%'>
							<Flex flexDirection='column' h='100%' p='22px' minW='60%' lineHeight='1.6'>
								<Text fontSize='34px' color='#fff' fontWeight='bold' mb='18px'>
									Welcome Back,
								</Text>
								<Text fontSize='md' color='#fff' fontWeight='normal' mb='auto'>
									Glad to see you again! <br />
									
								</Text>
								<Spacer />
								<Flex align='center'>
									<Button
										p='0px'
										variant='no-hover'
										bg='transparent'
										my={{ sm: '1.5rem', lg: '0px' }}>
										<Text
											fontSize='sm'
											color='#fff'
											fontWeight='bold'
											cursor='pointer'
											transition='all .3s ease'
											my={{ sm: '1.5rem', lg: '0px' }}
											_hover={{ me: '4px' }}>
											Ask me anything
										</Text>
										<Icon
											as={BsArrowRight}
											w='20px'
											h='20px'
											color='#fff'
											fontSize='2xl'
											transition='all .3s ease'
											mx='.3rem'
											cursor='pointer'
											pt='4px'
											_hover={{ transform: 'translateX(20%)' }}
										/>
									</Button>
								</Flex>
							</Flex>
						</Flex>
					</CardBody>
				</Card>
			
				{/* Satisfaction Rate */}
				<Card gridArea={{ md: '2 / 1 / 3 / 2', '2xl': 'auto' }} bgImage={medusa1} bgPosition='50%'>
					<CardHeader mb='24px'>
						<Flex direction='column'>
							<Text color='#fff' fontSize='28px' fontWeight='bold' mb='4px'>
								{"\n"}
								Edit Audio
							</Text>
							
						</Flex>
					</CardHeader>
					
				</Card>
				{/* Referral Tracking */}
				<Card gridArea={{ md: '2 / 2 / 3 / 3', '2xl': 'auto' }} bgImage={medusa1} bgPosition='50%'>
					<Flex direction='column'>
						<Flex justify='space-between' align='center' mb='130px'>
							<Text color='#fff' fontSize='28px' fontWeight='bold'>
								Edit Videos
							</Text>
							
						</Flex>
						
					</Flex>
					
				</Card>
			</Grid>
			{/* Add here */}
			<SimpleGrid columns={{ sm: 1, md: 2, xl: 4 }} spacing='18px'>
				{/* Combine */}
				<Card bgImg = {combine} bgPosition='50%' bgSize='cover' >
					<CardBody mb='100px'>
					</CardBody>
		
				</Card>
				{/* Crop/Trim */}
				<Card bgImg = {trim} bgPosition='50%' bgSize='cover' >
					<CardBody mb='100px'>
					</CardBody>
				</Card>
				{/* Combine */}
				<Card>
					<CardBody>
						<Flex flexDirection='row' align='center' justify='center' w='100%'>
							<Stat me='auto'>
								<Flex>
									<StatNumber fontSize='lg' color='#fff'>
										Combine
									</StatNumber>
									<StatHelpText
										alignSelf='flex-end'
										justifySelf='flex-end'
										m='0px'
										color='green.400'
										fontWeight='bold'
										ps='3px'
										fontSize='md'>
										+55%
									</StatHelpText>
								</Flex>
							</Stat>
						</Flex>
					</CardBody>
				</Card>
				{/* Crop/Trim */}
				<Card>
					<CardBody>
						<Flex flexDirection='row' align='center' justify='center' w='100%'>
							<Stat me='auto'>
								<Flex>
									<StatNumber fontSize='lg' color='#fff'>
										Crop/Trim
									</StatNumber>
									<StatHelpText
										alignSelf='flex-end'
										justifySelf='flex-end'
										m='0px'
										color='green.400'
										fontWeight='bold'
										ps='3px'
										fontSize='md'>
										+55%
									</StatHelpText>
								</Flex>
							</Stat>
						</Flex>
					</CardBody>
				</Card>
				{/* Autocaptions */}
				<Card bgImg = {autocaptions} bgPosition='50%' bgSize='cover' >
					<CardBody mb='100px'>
					</CardBody>
		
				</Card>
				{/* Denoising */}
				<Card bgImg = {denoise}  bgSize='cover' >
					<CardBody mb='100px'>
					</CardBody>
		
				</Card>
				{/* AutoCaptions */}
				<Card>
					<CardBody>
						<Flex flexDirection='row' align='center' justify='center' w='100%'>
							<Stat me='auto'>
								<Flex>
									<StatNumber fontSize='lg' color='#fff'>
										Autocaptions
									</StatNumber>
									<StatHelpText
										alignSelf='flex-end'
										justifySelf='flex-end'
										m='0px'
										color='green.400'
										fontWeight='bold'
										ps='3px'
										fontSize='md'>
										+55%
									</StatHelpText>
								</Flex>
							</Stat>
						</Flex>
					</CardBody>
				</Card>
				{/* Denoising */}
				<Card>
					<CardBody>
						<Flex flexDirection='row' align='center' justify='center' w='100%'>
							<Stat me='auto'>
								
								<Flex>
									<StatNumber fontSize='lg' color='#fff'>
										Denoising
									</StatNumber>
									<StatHelpText
										alignSelf='flex-end'
										justifySelf='flex-end'
										m='0px'
										color='green.400'
										fontWeight='bold'
										ps='3px'
										fontSize='md'>
										+55%
									</StatHelpText>
								</Flex>
							</Stat>
							
						</Flex>
					</CardBody>
				</Card>
				{/* Colour Correction */}
				<Card bgImg = {colourcorrection} bgPosition='50%' bgSize='cover' >
					<CardBody mb='100px'>
					</CardBody>
		
				</Card>
				{/* Compression */}
				<Card bgImg = {compression} bgPosition='50%' bgSize='cover' >
					<CardBody mb='100px'>
					</CardBody>
				</Card>
				{/* Colour Correction */}
				<Card>
					<CardBody>
						<Flex flexDirection='row' align='center' justify='center' w='100%'>
							<Stat me='auto'>
								
								<Flex>
									<StatNumber fontSize='lg' color='#fff'>
										Colour Correction
									</StatNumber>
									<StatHelpText
										alignSelf='flex-end'
										justifySelf='flex-end'
										m='0px'
										color='green.400'
										fontWeight='bold'
										ps='3px'
										fontSize='md'>
										+55%
									</StatHelpText>
								</Flex>
							</Stat>
							
						</Flex>
					</CardBody>
				</Card>
				{/* Compression */}
				<Card minH='83px'>
					<CardBody>
						<Flex flexDirection='row' align='center' justify='center' w='100%'>
							<Stat me='auto'>
								
								<Flex>
									<StatNumber fontSize='lg' color='#fff'>
										Compression (Resolution)
									</StatNumber>
									<StatHelpText
										alignSelf='flex-end'
										justifySelf='flex-end'
										m='0px'
										color='green.400'
										fontWeight='bold'
										ps='3px'
										fontSize='md'>
										+5%
									</StatHelpText>
								</Flex>
							</Stat>
							
						</Flex>
					</CardBody>
				</Card>
				{/* Speed Up/Down */}
				<Card bgImg = {speed} bgPosition='80%' bgSize='cover' >
					<CardBody mb='100px'>
					</CardBody>
		
				</Card>
				{/* Add Bg Music */}
				<Card bgImg = {bgmusic} bgPosition='50%' bgSize='cover' >
					<CardBody mb='100px'>
					</CardBody>
				</Card>
				{/* Speed Up/Down */}
				<Card>
					<CardBody>
						<Flex flexDirection='row' align='center' justify='center' w='100%'>
							<Stat>
								<Flex>
									<StatNumber fontSize='lg' color='#fff'>
										Speed Up/Down
									</StatNumber>
									<StatHelpText
										alignSelf='flex-end'
										justifySelf='flex-end'
										m='0px'
										color='red.500'
										fontWeight='bold'
										ps='3px'
										fontSize='md'>
										-14%
									</StatHelpText>
								</Flex>
							</Stat>
							<Spacer />
						</Flex>
					</CardBody>
				</Card>
				{/* Add Bg Music */}
				<Card>
					<CardBody>
						<Flex flexDirection='row' align='center' justify='center' w='100%'>
							<Stat me='auto'>
								<Flex>
									<StatNumber fontSize='lg' color='#fff' fontWeight='bold'>
										Add Background Music
									</StatNumber>
									<StatHelpText
										alignSelf='flex-end'
										justifySelf='flex-end'
										m='0px'
										color='green.400'
										fontWeight='bold'
										ps='3px'
										fontSize='md'>
										+8%
									</StatHelpText>
								</Flex>
							</Stat>
						</Flex>
					</CardBody>
				</Card>
			</SimpleGrid>
			
			<Grid templateColumns={{ sm: '1fr', md: '1fr 1fr', lg: '2fr 1fr' }} gap='24px'>
							</Grid>
		</Flex>
	);
}
