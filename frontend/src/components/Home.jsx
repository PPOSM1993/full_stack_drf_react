import { useEffect, useMemo, useState } from 'react'
import { Box, Chip, Typography, IconButton } from '@mui/material'
import CalendarViewMonthIcon from '@mui/icons-material/CalendarViewMonth';
import { MaterialReactTable } from 'material-react-table';
import AxiosInstance from './Axios';
import { Button } from '@mui/material';
import { Link } from 'react-router'
import AddBoxIcon from '@mui/icons-material/AddBox';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
const Home = () => {

    const [myData, setMyData] = useState([])

    const GetData = () => {
        AxiosInstance.get(`football_club/`).then((res) => {
            setMyData(res.data)
        })
    }

    useEffect(() => {
        GetData()
    }, [])

    const columns = useMemo(
        () => [
            {
                accessorKey: 'name',
                header: 'Name'
            },
            {
                accessorKey: 'country_details.name',
                header: 'Country'
            },
            {
                accessorKey: 'league_details.name',
                header: 'League'
            },
            {
                accessorKey: 'city',
                header: 'City'
            },
            {
                accessorKey: 'attendance',
                header: 'Attendance'
            },
            {
                accessorKey: 'characteristics_names',
                header: 'Characteristics',
                Cell: ({ cell }) => (
                    <div style={{ display: 'flex', gap: '8px', flexWrap: 'wrap' }}>
                        {
                            cell.getValue()?.map((char, index) => (
                                <Chip key={index} label={char} />
                            ))
                        }

                    </div>
                )
            }


        ]
    )

    return (
        <div>
            <Box className={"TopBar"}>
                <CalendarViewMonthIcon />
                <Typography sx={{ marginLeft: '15px', fontWeight: 'bold' }} variant='subtitle2'>View all clubs!</Typography>
            </Box>

            <MaterialReactTable
                columns={columns}
                data={myData}
                enableRowActions
                renderRowActions={({row}) => (
                    <Box sx={{display: 'flex',flexWrap:'nowrap', gap:'8px'}}>
                        <IconButton color="primary" component={Link} to={`edit/${row.original.id}`}> 
                            <EditIcon/>
                        </IconButton>

                        <IconButton color="error" component={Link} to={`delete/${row.original.id}`}> 
                            <DeleteIcon/>
                        </IconButton>
                    </Box>
                )
                }

            />


            <div>
                <Box sx={{ marginTop: '30px' }}>
                    <Button type="submit" variant="contained" component={Link} to="/create">
                        <AddBoxIcon />  Create Club
                    </Button>
                    
                </Box>
            </div>


        </div>
    )
}

export default Home